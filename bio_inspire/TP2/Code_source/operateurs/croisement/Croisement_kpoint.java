package operateurs.croisement;

import representation.Solution;

public class Croisement_kpoint extends Croisement{
    
        private int k;
    
        public Croisement_kpoint(Solution parent1, Solution parent2, double proba, int k) {
            super(parent1, parent2, proba);
            this.k = k;
        }
    
        @Override
        public void croiser() {
    
            int nb_variables_decision = parent1.getNb_variables_decision();
    
            enfant1 = new Solution(parent1);
            enfant2 = new Solution(parent2);
    
            double aleatoire = Math.random(); 
    
            int[] points_croisement = new int[k]; 
    
            if (aleatoire <= proba) {


                // Generation des points de croisements
                for (int i = 0; i < k; i++) {
                    points_croisement[i] = (int)(Math.random() * nb_variables_decision); 
                }

                // Croisement en fonction de si i est pair ou impair
                for (int i = 0; i < k; i++) {
                    if (i % 2 == 0) {
                        for (int j = 0; j < points_croisement[i]; j++) {
                            enfant1.setVariable(j, parent1.getDoubleVariable(j));
                            enfant2.setVariable(j, parent2.getDoubleVariable(j));
                        }
                    } else {
                        for (int j = 0; j < points_croisement[i]; j++) {
                            enfant1.setVariable(j, parent2.getDoubleVariable(j));
                            enfant2.setVariable(j, parent1.getDoubleVariable(j));
                        }
                    }
                }

                //Ajout du dernier morceau
                for (int i = points_croisement[k - 1]; i < nb_variables_decision; i++) {
                    enfant1.setVariable(i, parent1.getDoubleVariable(i));
                    enfant2.setVariable(i, parent2.getDoubleVariable(i));
                }
    
            }
    
        }
    
}
