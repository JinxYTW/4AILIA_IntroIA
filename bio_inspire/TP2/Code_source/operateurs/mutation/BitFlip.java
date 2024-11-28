package operateurs.mutation;

import representation.Solution;

public class BitFlip extends Mutation {

    public BitFlip(double proba) {
        super(proba);
    }

    @Override
    public Solution muter(Solution solution) {

        if (Math.random() < proba) {
            int n = solution.getNb_variables_decision(); // Taille du chromosome

            for (int i = 0; i < n; i++) {
                int bit = solution.getIntVariable(i); // Récupérer la valeur du gène
                solution.setVariable(i, 1 - bit); // Inverser le bit
            }
        }

        
        return solution;
    }
    
}
