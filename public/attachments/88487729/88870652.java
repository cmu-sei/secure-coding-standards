public class MissedSignal implements Runnable {
  private static Object lock = new Object();
  private static int buffer_count = 5;
  private static int number; // Selects function based on thread number	
  
  public void setThreadNumber(int num) {
    number = num;
  }

  public void run (){
    synchronized(lock) {
      try {    	  
        if(number == 1) {	  
          System.out.println("Thread 1 started..."); 
          while(buffer_count == 0) { 
      	    System.out.println("Beginning wait() Thread 1...");	
      	    lock.wait();		  
      	    System.out.println("Thread 1 got notified this time...");
      	  }  
      	  System.out.println("Exiting because Thread 1 condition is false...");	

      	} else if(number == 2) {  	    		  
      	  System.out.println("Thread 2 started...");
      	  while(buffer_count == 10) {	
      	    System.out.println("Beginning wait() Thread 2...");	
      	    lock.wait();   	    		    	        	    
      	    System.out.println("Thread 2 got notified this time...");
      	  }
      	  System.out.println("Exiting because the thread 2 condition is false...");

      	} else if(number == 3) {	   
          lock.notify();      	   		  
        } 	    	  
      } catch (InterruptedException ie) {
        // Handle the exception
      }
    }	  
  }

  public static void makeThread1True() {
    buffer_count = 0;
  }
        
  public static void makeThread2True() {
    buffer_count = 10;
  }
        
  public static void main(String[] args) throws IOException, InterruptedException {    
    MissedSignal ms = new MissedSignal();
    
    makeThread1True();
    ms.setThreadNumber(1);
    new Thread(ms).start();
      
    Thread.sleep(1000);
   
    makeThread2True();
    ms.setThreadNumber(2);
    new Thread(ms).start();
   
    Thread.sleep(1000);
      
    ms.setThreadNumber(3);
    new Thread(ms).start();    
  }
}
