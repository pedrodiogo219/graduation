class Counter {
    private int c = 0;

    public int increment() {
        return ++c;
    }

    public int decrement() {
        return --c;
    }

    public int value() {
        return c;
    }
}


public class HelloThread extends Thread {
	private	Counter c;
    
    public void run() {
        int i;
        for (i = 0; i < 20; i++){
        	c.increment();
        	system.out.Println( this.getName() + " -> " + toString(c.value()));
        }
        
    }

    public static void main(String args[]) {
        Thread t[10];
        int i;
        Counter myCounter = new Counter();
        for(i = 0; i < 10; i++){
			t[i] = new HelloThread();
			t[i].c = myCounter;
		}	
        t.start();
    }
}


