package operateurs.selection;

import java.util.ArrayList;

import representation.Solution;

public class Roulette_wheel_selection extends Selection {

    public Roulette_wheel_selection(ArrayList<Solution> population) {
        super(population);
    }

    @Override

    public Solution selectionner() {
        double somme = 0.0;
        double sommef = 0.0;
        for (Solution solution : population) {
            somme += solution.getFitness();
            sommef += solution.getF(); 
        }
        double random = Math.random() * sommef;

        double somme2 = 0.0;
        double sommef2 = 0.0;
        for (Solution solution : population) {
            sommef2 += solution.getF();
            if (sommef2 >= random) {
                return solution;
            }
        }
        return null;
    }
    
}
