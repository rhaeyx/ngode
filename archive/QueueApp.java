import java.util.Scanner;

// Queue.java
// demonstrates queue
// to run this program: C>java QueueApp
////////////////////////////////////////////////////////////////
class Queue {
   private int maxSize;
   private long[] queArray;
   private int front;
   private int rear;
   private int nItems;

   // --------------------------------------------------------------
   public Queue(int s) // constructor
   {
      maxSize = s;
      queArray = new long[maxSize];
      front = 0;
      rear = -1;
      nItems = 0;
   }

   // --------------------------------------------------------------
   public void insert(long j) // put item at rear of queue
   {
      if (rear == maxSize - 1) // deal with wraparound
         rear = -1;
      queArray[++rear] = j; // increment rear and insert
      nItems++; // one more item
   }

   // --------------------------------------------------------------
   public long remove() // take item from front of queue
   {
      long temp = queArray[front++]; // get value and incr front
      if (front == maxSize) // deal with wraparound
         front = 0;
      nItems--; // one less item
      return temp;
   }

   // --------------------------------------------------------------
   public long peekFront() // peek at front of queue
   {
      return queArray[front];
   }

   // --------------------------------------------------------------
   public boolean isEmpty() // true if queue is empty
   {
      return (nItems == 0);
   }

   // --------------------------------------------------------------
   public boolean isFull() // true if queue is full
   {
      return (nItems == maxSize);
   }

   // --------------------------------------------------------------
   public int size() // number of items in queue
   {
      return nItems;
   }
   // --------------------------------------------------------------
} // end class Queue
  ////////////////////////////////////////////////////////////////

class QueueApp {
   public static void main(String[] args) {
      Scanner input = new Scanner(System.in);

      int N = input.nextInt();
      Queue theQueue = new Queue(N); // queue holds N items

      int count = 1;
      int line = 0;
      int counter = 0;
      int pakganern = -1; // -1 pak, 1 ganern
      while (line < N) {
         for (int k = 0; k < count; k++) {
            if (line < N) {
               theQueue.insert(pakganern);
               line++;
            }
         }

         counter++;

         if (counter % 2 == 0) {
            count++;
         }

         pakganern *= -1;
      }

      while (!theQueue.isEmpty()) // remove and display
      { // all items
         long n = theQueue.remove(); //
         if (n == -1) {
            System.out.println("PAK");
         } else {
            System.out.println("GANERN");
         }
      }

      input.close();
   } // end main()
} // end class QueueApp
  ////////////////////////////////////////////////////////////////
