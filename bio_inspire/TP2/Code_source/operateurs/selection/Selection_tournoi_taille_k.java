package operateurs.selection;

import java.util.ArrayList;

import representation.Solution;

public class Selection_tournoi_taille_k extends Selection {

    private int k;

    public Selection_tournoi_taille_k(ArrayList<Solution> population, int k) {
        super(population);
        this.k = k;
    }

    @Override
    public Solution selectionner() {
        ArrayList<Solution> tournoi = new ArrayList<Solution>();

        for (int i = 0; i < k; i++) {
            int index = (int) (Math.random() * population.size());
            tournoi.add(population.get(index));
        }
        
        return getBestSolution(tournoi);
    }

    public Solution getBestSolution(ArrayList<Solution> tournoi) {
        Solution best = tournoi.get(0);
        for (int i = 1; i < tournoi.size(); i++) {
            if (tournoi.get(i).getF() < best.getF()) {
                best = tournoi.get(i);
            }
        }
        return best;
    }
    
}
