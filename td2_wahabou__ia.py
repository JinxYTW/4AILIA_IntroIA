import random


def roulette_wheel_selection(population, fitness):
    # Compute the sum of all fitness values
    total_fitness = sum(fitness)
    # Probability of selecting each individual
    probabilities = [f / total_fitness for f in fitness]
    # Cumulative probability of selecting each individual
    cumulative_probabilities = [sum(probabilities[:i+1]) for i in range(len(probabilities))]
    # Select a random number between 0 and 1
    r = random.random()
    # Find the index of the individual to select
    for i, p in enumerate(cumulative_probabilities):
        if r <= p:
            return population[i]
        
print(roulette_wheel_selection(["A", "B", "C", "D"], [12, 8, 6, 4]))

def tournament_selection(population, fitness, tournament_size):
    # Sélectionner aléatoirement tournament_size indices
    indices = random.sample(range(len(population)), tournament_size)
    
    # Trouver l'individu avec la meilleure fitness parmi les sélectionnés
    meilleur_individu_index = max(indices, key=lambda i: fitness[i])
    
    # Retourner l'individu sélectionné
    return population[meilleur_individu_index]
print(tournament_selection(["A", "B", "C", "D"], [12, 8, 6, 4],2))

def tournament_selection_zip(population, fitness, tournament_size):
    # Sélectionner des individus aléatoirement pour le tournoi
    tournoi = random.sample(list(zip(population, fitness)), tournament_size)
    
    # Trouver l'individu avec la meilleure forme physique (fitness)
    meilleur_individu = max(tournoi, key=lambda x: x[1])
    
    # Retourner l'individu sélectionné
    return meilleur_individu[0]
print(tournament_selection_zip(["A", "B", "C", "D"], [12, 8, 6, 4],2))

def croisement_1point(parent1, parent2):
    # Sélectionner un point de croisement aléatoire
    point = random.randint(1, len(parent1) - 1)
    
    # Créer les enfants en croisant les parents au point de croisement
    enfant1 = parent1[:point] + parent2[point:]
    enfant2 = parent2[:point] + parent1[point:]
    
    return enfant1, enfant2

print(croisement_1point("010101", "101010"))

def croisement_kpoint(parent1, parent2, k):
    # Sélectionner k points de croisement aléatoires
    points = sorted(random.sample(range(1, len(parent1)), k))
    print(points)
    
    # Initialiser les enfants
    enfants = [parent1[:points[0]], parent2[:points[0]]]
    
    # Créer les enfants en croisant les parents aux points de croisement
    for i in range(1, len(points)):
        if i % 2 == 0:
            enfants[0] += parent1[points[i-1]:points[i]]
            enfants[1] += parent2[points[i-1]:points[i]]
        else:
            enfants[0] += parent2[points[i-1]:points[i]]
            enfants[1] += parent1[points[i-1]:points[i]]
    
    # Ajouter la dernière partie des parents
    if len(points) % 2 == 0:
        enfants[0] += parent1[points[-1]:]
        enfants[1] += parent2[points[-1]:]
    else:
        enfants[0] += parent2[points[-1]:]
        enfants[1] += parent1[points[-1]:]
    
    return enfants

print(croisement_kpoint("010101", "101010", 2))

