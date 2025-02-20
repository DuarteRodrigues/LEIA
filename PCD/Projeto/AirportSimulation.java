// Nº Aluno: a22206488
// Nome: Duarte Pinto Rodrigues
// Curso: LEIA
// UC: Programação Concorrente e Distribuída
// 1º Trabalho Prático 1 - Simulação de um Aeroporto

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.Random;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class AirportSimulation{
    // Airport Configurations
    private static final int NUM_RUNWAYS = 2;                       // Number of airport runways
    private static final int TAKEOFF_DURATION = 2;                  // In time units
    private static final int LANDING_DURATION = 3;                  // In time units
    private static final int MAX_QUEUE_SIZE = 10; 
    private static int time = 0;                  // Waiting queue max size
    private static final int SIMULATION_TIME = 1440;                // 24H in time units
    private static final int TIME_UNIT_MS = 10;                     // Time unit = 10ms
    private static final double ARRIVAL_RATE = 0.2;                // Rate of arrival (avg. of 1 every 4 minutes)
    private static final double DEPARTURE_RATE = 0.2;               // Rate of departure (avg. of 1 every 5 minutes)
    private static final double MALFUNCTION_PROBABILITY = 0.0024;    // Percentage probability of a plane malfunction

    // Queues for departure and arrival management
    private final Queue<Flight> arrivalsQueue = new LinkedList<>();
    private final Queue<Flight> departuresQueue = new LinkedList<>();
    private final List<Runway> runways = new ArrayList<>();
    private final Random random = new Random();

    // All around stats
    private int divertedFlights = 0;    // Redirected flights count 
    private int cancelledFlights = 0;   // Cancelled flights count

    // Initializing to construct the runways
    public AirportSimulation() {
        for (int i = 0; i < NUM_RUNWAYS; i++){
            runways.add(new Runway(i+1));
        }
    }

    public static void main(String [] args){
        AirportSimulation simulation = new AirportSimulation();
        simulation.runSimulation();
    } 

    // Main method to execute the simulation. It creates flights, processes runways and collects statistics.
    private void runSimulation(){
        ExecutorService executor = Executors.newCachedThreadPool();

        // Simulation's main loop
        for (time = 0; time < SIMULATION_TIME; time ++){
            // Processing of new flights
            processArrivals(executor);    // Processes arrivals
            processDepartures(executor);  // Processes departures
            //processRunways();             // Allocates flights to runways

            try {
                Thread.sleep(TIME_UNIT_MS);         // Moves time forward in the simulation
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        }

        executor.shutdown();    // Finalize the pending threads
        printStatistics();      // Display final statistics
    }

    // Processes arrivals, adding them to the arrival queue or diverted flights

    private void processArrivals( ExecutorService executor){
        int arrivals = Poisson.getRandom(ARRIVAL_RATE);
        for (int i = 0; i < arrivals; i++){
            if (random.nextDouble() < MALFUNCTION_PROBABILITY) {
                // Simulate a malfunction
                System.out.println(currentTime() + " A flight experienced a malfunction and was redirected.");
                divertedFlights++;
            } else if(arrivalsQueue.size() < MAX_QUEUE_SIZE ){
                // Normal processing
                Flight flight = new Flight("Arrival");
                arrivalsQueue.add(flight);
                new Thread(flight).start();
                System.out.println(currentTime() + " Flight " + flight.getId() + " added to arrivals queue.");
            } else {
                // Queue is full, divert the flight
                divertedFlights++;  // Increments the count of redirected flights
                System.out.println(currentTime() + " An arrival flight was diverted");
            }
        }
    }

    // Processes departures, adding them to the departure queue or cancelled flights

    private void processDepartures(ExecutorService executor){
        int departures = Poisson.getRandom(DEPARTURE_RATE);
        for (int i = 0; i < departures; i++) {
            if (random.nextDouble() < MALFUNCTION_PROBABILITY) {
                // Simulate a malfunction
                System.out.println(currentTime() + " A flight experienced a malfunction and was cancelled.");
                cancelledFlights++;
            } else if (departuresQueue.size() < MAX_QUEUE_SIZE) {
                Flight flight = new Flight("Departure");
                departuresQueue.add(flight);
                new Thread(flight).start();
                System.out.println(currentTime() + " Flight " + flight.getId() + " added to departures queue.");
            } else {
                cancelledFlights++; // Increments the count of redirected flights
                System.out.println(currentTime() + " A departure flight was cancelled.");
            }
        }
    }

    // Processes runway management, asserting flights to land and takeoff, if available

    private void processRunways(){
        for (Runway runway : runways) {
            if (!runway.isBusy() && !arrivalsQueue.isEmpty()) {
                Flight flight = arrivalsQueue.poll();
                runway.assignRunway(flight, LANDING_DURATION);
            } else if (!runway.isBusy() && !departuresQueue.isEmpty()) {
                Flight flight = departuresQueue.poll();
                runway.assignRunway(flight, TAKEOFF_DURATION);
            }
        }
    }

    // Displays the final stats at the end of the simulation

    private void printStatistics(){
        System.out.println("\nSimulation Statistic:");
        System.out.println("Total Diverted Flights: " + divertedFlights);
        System.out.println("Total Cancelled Flights: " + cancelledFlights);
        for (Runway runway : runways){
            runway.printStats();
        }
    }

    // Converts the time units into a readable string (hh:mm)

    private static String currentTime(){
        return (time/60) + ":" + String.format("%02d", time % 60);
    }

    // Class that represents a flight
    private class Flight implements Runnable{
        private static int counter = 0; // Global counter for unique IDs
        private final int id;
        private final String type;

        public Flight (String type){
            this.id = ++counter;
            this.type = type;
            System.out.println(AirportSimulation.currentTime() + " A flight with ID " + id + " was created.");
        }

        public int getId(){
            return id;
        }

        public String getType(){
            return type;
        }

        @Override
        public void run(){
            boolean assigned = false;
            do{
                for (Runway runway : runways) {
                    assigned = runway.assignRunway(this, type.equals("Arrival") ? LANDING_DURATION : TAKEOFF_DURATION);
                }
            }while (!assigned);
            
        }
    }

    // Class that represents a runway
    private class Runway{
        private final int id;
        private int landings = 0;
        private int takeoffs = 0;
        private boolean busy = false;

        public Runway(int id){
            this.id = id;
        }

        public boolean isBusy(){
            return busy;
        }

        // Attributes a flight to a runway to the execution(landing and takeoff)

        synchronized public boolean assignRunway(Flight flight, int duration){
            if (!isBusy()) {
                busy = true; 
                try {
                    Thread.sleep(duration * TIME_UNIT_MS);
                    System.out.println(AirportSimulation.currentTime() + " Flight " + flight.getId() + " assigned to Runway " + id + " for " + flight.getType().toLowerCase() + ".");
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                }
                if (flight.type.equals("Arrival")){
                    System.out.println("Arrival Queue: " + arrivalsQueue.size());
                    arrivalsQueue.poll(); 
                    landings++;
                 } else { 
                    System.out.println("Departure Queue: " + departuresQueue.size());
                    departuresQueue.poll();
                    takeoffs++;
                 }
                busy = false;
                return true;
            } else {
                return false;
            }
            
        }

        // Displays the usability stats of the runway

        public void printStats(){
            System.out.println("Runway " + id + ": " + landings + " landings, " + takeoffs + " takeoffs.");
        }

    }

    // Class to generate random events on the basis of the Poisson distribution
    private static class Poisson {
        private static final Random random = new Random();

        public static int getRandom(double mean) {
            double L = Math.exp(-mean);
            int k = 0;
            double p = 1.0;
            do {
                k++;
                p *= random.nextDouble();
            } while (p > L);
            return k - 1;
        }
    }
}


// There are planes still in queue when the day is over, dispatch the last flights before closing the day in the airport 
