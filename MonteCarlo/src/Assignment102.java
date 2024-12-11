// Estimate the value of Pi using Monte-Carlo Method, using parallel program
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.atomic.AtomicInteger;
class PiMonteCarlo {
	AtomicInteger nAtomSuccess;
	int nThrows;
	double value;
	class MonteCarlo implements Runnable {
		@Override
		public void run() {
			double x = Math.random();
			double y = Math.random();
			if (x * x + y * y <= 1)
				nAtomSuccess.incrementAndGet();
		}
	}
	public PiMonteCarlo(int i) {
		this.nAtomSuccess = new AtomicInteger(0);
		this.nThrows = i;
		this.value = 0;
	}
	public double getPi() {
		int nProcessors = Runtime.getRuntime().availableProcessors();
		ExecutorService executor = Executors.newWorkStealingPool(nProcessors);
		for (int i = 1; i <= nThrows; i++) {
			Runnable worker = new MonteCarlo();
			executor.execute(worker);
		}
		executor.shutdown();
		while (!executor.isTerminated()) {
		}
		value = 4.0 * nAtomSuccess.get() / nThrows;
		return value;
	}
}

public class Assignment102 {
	public static void main(String[] args) {
		int numIterations = 1000000;
		PiMonteCarlo PiVal = new PiMonteCarlo(numIterations);

		String outputFilePath = "pi_res_G26.csv";

		long startTime = System.currentTimeMillis();
		double value = PiVal.getPi();
		long stopTime = System.currentTimeMillis();
		long duration = stopTime - startTime;

		WriteFile.writeResult(outputFilePath, numIterations, value, duration, PiVal);

		System.out.println("Nombre d'itérations (Ntot): " + numIterations);
		System.out.println("Pi: " + value);
		System.out.println("Time Duration: " + duration + "ms");
		System.out.println("Available processors: " + Runtime.getRuntime().availableProcessors());
		System.out.println("Nombre de points : " + PiVal.nAtomSuccess);
		System.out.println("Error: " + ((value - Math.PI) / Math.PI));
		//System.out.println("Difference to exact value of pi: " + (value - Math.PI));
	}
}
