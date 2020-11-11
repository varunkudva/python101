package com.github.varunkudva;

import java.text.DateFormat;
import java.time.Instant;
import java.time.LocalDateTime;
import java.time.ZoneId;
import java.util.Date;
import java.util.EmptyStackException;
import java.util.HashMap;
import java.util.Stack;

enum SpotType {
    BIKE, CAR, VAN;
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
    Spot spot;

    public Ticket() {
        // Empty constructor. Can replace with a design pattern
    }

    public Ticket generateTicket(Long ticketNumber, Spot spot) {
        this.ticketNumber = ticketNumber;
        this.entryTime = System.currentTimeMillis()/1000;
        this.spot = spot;
        return this;
    }

    @Override
    public String toString() {
        LocalDateTime ldt;
        ldt = Instant.ofEpochMilli(this.entryTime).atZone(ZoneId.systemDefault()).toLocalDateTime();
        return (String.format("Ticket number: %d, EntryTime %s, spot: %s", this.ticketNumber, ldt, this.spot));
    }
}

class Pricing {
    HashMap<Spot, Double> PriceMap = new HashMap<Spot, Double>();

    Double getPrice(SpotType sType) {
        return Double.valueOf(0);
    }

    void setPrice(SpotType sType, double Price) {

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
    HashMap<Long, Ticket> ticketHash;
    Long ticketNumber;

    private ParkingLot(String name, String location) {
        this.name = name;
        this.location = location;
        this.spotPool = new HashMap<>();
        this.ticketHash = new HashMap<>();
        this.ticketNumber = Long.valueOf(1);
    }

    synchronized long getNextTicketNumber() {
        Long ticketNumber = this.ticketNumber;
        this.ticketNumber += 1;
        return ticketNumber;
    }

    public void addSpots(SpotType v, int totalSpots) {
        Stack spotStack = new Stack<Spot>();
        for (int i = 0; i < totalSpots; i++) {
            Spot spot = new Spot(i, v);
            spotStack.push(spot);
        }
        spotPool.put(v, spotStack);
    }

    public Spot getSpot(SpotType sType) throws EmptyStackException {
        Spot spot = (Spot) spotPool.get(sType).pop();
        return spot;
    }

    public Ticket getTicket(SpotType sType) throws Exception {
        Ticket tkt;
        try {
            Spot spot = getSpot(sType);
            tkt = new Ticket().generateTicket(getNextTicketNumber(), spot);
            this.ticketHash.put(tkt.ticketNumber, tkt);
            return tkt;
        } catch (EmptyStackException e) {
//            System.out.println("No free spots of type %s", sType);
        }
        return null;
    }

    public void payTicket(Long ticketNum) {
        try {
            Ticket tkt = this.ticketHash.get(ticketNum);
            Long currentTime = System.currentTimeMillis();
            Long parkingHours = (currentTime - tkt.entryTime)/3600;
//            Double price = Pricing
//            Double Amount = parkingHours *
        } catch (Exception e) {

        }
    }

    public static void main(String[] args) throws Exception {
        ParkingLot myLot = new ParkingLot("NewarkLot", "94560");
        // Can use builder here for parking lot builder
        myLot.addSpots(SpotType.BIKE, 10);
        myLot.addSpots(SpotType.CAR, 10);
        myLot.addSpots(SpotType.VAN, 10);
        System.out.println(myLot.getTicket(SpotType.CAR));
    }
}
