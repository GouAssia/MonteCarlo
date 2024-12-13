// Estimate the value of Pi using Monte-Carlo Method, using parallel program
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.atomic.AtomicInteger;

class PiMonteCarlo {
	AtomicInteger nAtomSuccess;
	int nThrows;
	double value;
	int nProcessors;
	class MonteCarlo implements Runnable {
		@Override
		public void run() {
			double x = Math.random();
			double y = Math.random();
			if (x * x + y * y <= 1)
				nAtomSuccess.incrementAndGet();
		}
	}
	public PiMonteCarlo(int i, int nbProcessor) {
		this.nAtomSuccess = new AtomicInteger(0);
		this.nThrows = i;
		this.value = 0;
		this.nProcessors = nbProcessor;
	}
	public double getPi() {
		//int nProcessors = Runtime.getRuntime().availableProcessors();
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
		System.out.println(Integer.parseInt(args[0]));
		for (int i = 0; i < 5; i++) {
		int numIterations = 16000000;
		int nbProcessor = 16;
		PiMonteCarlo PiVal = new PiMonteCarlo(numIterations, nbProcessor);

		String outputFilePath = "assignment102_stabFaible_PCperso.csv";

		long startTime = System.currentTimeMillis();
		double value = PiVal.getPi();
		long stopTime = System.currentTimeMillis();
		long duration = stopTime - startTime;

		WriteFile.writeResult(outputFilePath, numIterations, value, duration, PiVal, nbProcessor);

		System.out.println("Nombre d'itérations (Ntot): " + numIterations);
		System.out.println("Pi: " + value);
		System.out.println("Time Duration: " + duration + "ms");
		System.out.println("Nombre processeur: " + nbProcessor);
		System.out.println("Nombre de points : " + PiVal.nAtomSuccess);
		System.out.println("Error: " + ((value - Math.PI) / Math.PI));
		//System.out.println("Difference to exact value of pi: " + (value - Math.PI));
		}
	}
}
