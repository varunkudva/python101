package com.github.varunkudva;

import java.text.DateFormat;
import java.util.Date;
import java.util.HashMap;
import java.util.Stack;

enum SpotType {
    BIKE, CAR, VAN
}

class Spot {
    Integer SpotNumber;
    SpotType SpotType;

    public Spot(Integer spotNumber, com.github.varunkudva.SpotType spotType) {
        SpotNumber = spotNumber;
        SpotType = spotType;
    }

    @Override
    public String toString() {
        return (String.format("Spot Type: %s, Number %d", SpotType, SpotNumber));
    }
}

class Ticket {
    Long ticketNumber;
    long entryTime;
    Spot    spot;

    public Ticket() {
        // Empty constructor. Can replace with a design pattern
    }

    public Ticket generateTicket(Long ticketNumber, Spot spot) {
        this.ticketNumber = ticketNumber;
        this.entryTime = System.currentTimeMillis();
        this.spot = spot;
        return this;
    }

    @Override
    public String toString() {
        return (String.format("Ticket number: %d, EntryTime %s, spot: %s", this.ticketNumber, DateFormat., this.spot));
    }
}

public class ParkingLot {
    /*
    single floor
    single entrance exit
    getTicket()
    getSpot()
    isFull()
    payTicket()
     */
    String name;
    String location;
    HashMap<SpotType, Stack> spotPool;
    Long ticketNumber;

    private ParkingLot(String name, String location) {
        this.name = name;
        this.location = location;
        this.spotPool = new HashMap<>();
        this.ticketNumber = Long.valueOf(1);
    }

    synchronized long getNextTicketNumber() {
        Long ticketNumber = this.ticketNumber;
        this.ticketNumber += 1;
        return ticketNumber;
    }

    public void addSpots(SpotType v, int totalSpots) {
        Stack spots = new Stack<Integer>();
        for (int i=0; i < totalSpots; i++) {
            spots.push(i);
        }
        spotPool.put(v, spots);
    }

    public Spot getSpot(SpotType sType) throws Exception {
        if (spotPool.get(sType).empty()) {
            throw new Exception(String.format("No free spots for Spot type %s", sType));
        }
        Integer spotNumber = (Integer) spotPool.get(sType).pop();
        return (new Spot(spotNumber, sType));
    }

    public Ticket getTicket(SpotType sType) throws Exception {
        Spot spotNumber = getSpot(sType);
        return new Ticket().generateTicket(getNextTicketNumber(), spotNumber);
    }

    public static void main(String[] args) throws Exception {
        ParkingLot myLot = new ParkingLot("NewarkLot", "94560");
        myLot.addSpots(SpotType.BIKE, 10);
        myLot.addSpots(SpotType.CAR, 10);
        System.out.println(myLot.getTicket(SpotType.CAR));

    }
}
