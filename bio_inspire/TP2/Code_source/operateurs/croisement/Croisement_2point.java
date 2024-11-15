package operateurs.croisement;

import representation.Solution;

public class Croisement_2point extends Croisement{

    public Croisement_2point(Solution parent1, Solution parent2, double proba) {
        super(parent1, parent2, proba);
    }

    @Override
    public void croiser() {

        int nb_variables_decision = parent1.getNb_variables_decision();

        enfant1 = new Solution(parent1);
        enfant2 = new Solution(parent2);

        double aleatoire = Math.random(); 

        int point_croisement1 = -1; 
        int point_croisement2 = -1; 

        if (aleatoire <= proba) {

            point_croisement1 = (int)(Math.random() * nb_variables_decision); 
            point_croisement2 = (int)(Math.random() * nb_variables_decision); 

            if (point_croisement1 > point_croisement2) {
                int temp = point_croisement1;
                point_croisement1 = point_croisement2;
                point_croisement2 = temp;
            }

            for (int i = 0; i < point_croisement1; i++) {
                enfant1.setVariable(i, parent1.getDoubleVariable(i));
                enfant2.setVariable(i, parent2.getDoubleVariable(i));
            }

            for (int i = point_croisement1; i < point_croisement2; i++) {
                enfant1.setVariable(i, parent2.getDoubleVariable(i));
                enfant2.setVariable(i, parent1.getDoubleVariable(i));
            }

            for (int i = point_croisement2; i < nb_variables_decision; i++) {
                enfant1.setVariable(i, parent1.getDoubleVariable(i));
                enfant2.setVariable(i, parent2.getDoubleVariable(i));
            }

        }

    }
}
