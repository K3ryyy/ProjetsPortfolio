#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define NBLIG 6
#define NBCOL 7
const char PION_A = 'X';
const char PION_B = 'O';
const char VIDE= ' ';
const char INCONNU = ' ';
const int COLONNE_DEBUT = (NBCOL+1)/2;

typedef char tab[NBLIG][NBCOL];

void initGrille(tab grille)
{
    int i, j;
    for (i=0;i<NBLIG;i++)
    {
        for (j=0;j<NBCOL;j++)
        {
            grille[i][j]=VIDE;
        }
    }

}


void afficheGrille(tab grille, char pion, int col)
{
    int i, j, espace;
    espace=0;
    system("clear");
    while (espace!=col-1)
    {
        printf("    ");
        espace=espace+1;
    }
    printf("  %c \n", pion);
    for (i = 0; i < NBLIG; i++)//Affichage de la grille
    {
        for (j = 0; j < NBCOL; j++)
        {
            if (j == 0)
            {
                printf("| %c |", grille[i][j]);//On affiche "|   |" seulement au premier élement d'une ligne pour ne pas afficher 2 "|" d'affilé
            }
            else
            {
                printf(" %c |", grille[i][j]);
            }
        }
        printf("\n+---+---+---+---+---+---+---+\n");
    }

    printf("  1   2   3   4   5   6   7\n");
}

bool grillePleine(tab grille)
{
    bool remplie = true;
    int i, j;
    for (i=0;i<NBLIG;i++)
    {
        for (j=0;j<NBCOL;j++)
        {
            if (grille[i][j] == VIDE)
            {
                remplie = false;
            }
        }
    }

    return remplie;
}

int choisirColonne(tab grille, char pion, int colonne)
{
    
    printf("Choisissez la colonne\n");
    scanf("%d",&colonne);
    while((colonne<1)||(colonne>7))
    {
        printf("Valeur impossible \n");
        printf("Choisissez la colonne\n");
        scanf("%d",&colonne);        
    }

    int i = colonne-1;

    return i;
}

int trouverLigne(tab grille, int colonne)
{
    int compteur = NBLIG-1;
    int resultat = -1;
    while (resultat == -1 && compteur >= 0)
    {
        if (grille[compteur][colonne] == VIDE)
        {
            resultat = compteur;
        }
        compteur--;
    }
    return resultat;
}

void jouer(tab grille, char pion, int *ligne, int *colonne)
{   
    bool plein=false;

    while(!plein)
    {
        *colonne=0;
        *ligne=0;

        *colonne=choisirColonne(grille, pion, *colonne);
        *ligne=trouverLigne(grille, *colonne);
        if (*ligne!=-1)
        {
            plein=true;
        }
    }
    grille[*ligne][*colonne]=pion;
   
}

bool estVainqueur(tab grille, int pion_ligne, int pion_colonne){
    char pion;
    bool victoire;
    int nbrPion, i;
    
    pion = grille[pion_ligne][pion_colonne];
    victoire = false;
    
    //Verticale
    if(victoire == false){
        i= 1;
        nbrPion = 1; //on vient juste de le mettre
        while(grille[pion_ligne + i][pion_colonne] == pion && pion_ligne + i < NBLIG){
            nbrPion++;
            i++;
        }
        //je commpte le nombre de pion au dessous
        i= 1;
        while(grille[pion_ligne - i][pion_colonne] == pion && pion_ligne  - i >=0){
            nbrPion++;
            i++;
        }
        
        if(nbrPion == 4){
            victoire = true;
        }
    }
    
    //horizontale
    if(victoire == false){
        i= 1;
        nbrPion = 1; //on vient juste de le mettre
        while(grille[pion_ligne][pion_colonne + i] == pion && pion_colonne + i < NBCOL){
            nbrPion++;
            i++;
        }
        //je commpte le nombre de pion au dessous
        i= 1;
        while(grille[pion_ligne][pion_colonne - i] == pion && pion_colonne  - i >=0){
            nbrPion++;
            i++;
        }
        
        if(nbrPion == 4){
            victoire = true;
        }
    }
    
    
    
    //diagonale
    if(victoire == false){
        i= 1;
        nbrPion = 1; //on vient juste de le mettre
        while(grille[pion_ligne - i][pion_colonne + i] == pion && pion_ligne - i >= 0 && pion_colonne + i < NBCOL){
            
            nbrPion++;
            i++;
        }
        
        i= 1;
        while(grille[pion_ligne + i][pion_colonne - i] == pion && pion_ligne + i < NBLIG && pion_colonne - i >= 0){
            
            nbrPion++;
            i++;
        }
        
        if(nbrPion == 4){
            victoire = true;
        }
    }
    
    
    if(victoire == false){
        i= 1;
        nbrPion = 1; //on vient juste de le mettre
        while(grille[pion_ligne + i][pion_colonne + i] == pion && pion_ligne + i < NBLIG && pion_colonne + i < NBCOL){
            
            nbrPion++;
            i++;
        }
        
        i= 1;
        while(grille[pion_ligne - i][pion_colonne - i] == pion && pion_ligne - i >= 0 && pion_colonne - i >= 0){
            
            nbrPion++;
            i++;
        }
        if(nbrPion == 4){
            victoire = true;
        }
    }
    
    return victoire;
}

void finPartie(char pionVainqueur)
{
    if (pionVainqueur==PION_A)
    {
        printf("Le pion X a gagne !");
    }
    else if(pionVainqueur==PION_B)
    {
        printf("Le pion O a gagne !");
    }
    else{
        printf("Egalite !");
    }
}

int main(void)
{
    int colonne;
    int ligne;
    tab grille;
    char vainqueur;
    

    initGrille(grille);
    vainqueur = INCONNU;
    afficheGrille(grille,PION_A,COLONNE_DEBUT);

    while ((vainqueur==INCONNU)&&(!grillePleine(grille)))
    {
        jouer(grille, PION_A,&ligne,&colonne);
        afficheGrille(grille,PION_B,COLONNE_DEBUT);
        if (estVainqueur(grille, ligne, colonne))
        {
            vainqueur=PION_A;
            
        }
        else if (!grillePleine(grille))
        {
            jouer(grille, PION_B, &ligne, &colonne);
            afficheGrille(grille, PION_A, COLONNE_DEBUT);
            if (estVainqueur(grille, ligne, colonne))
            {
                vainqueur=PION_B;
                
            }
        }
        finPartie(vainqueur);
        
    }
    
   
    
  
}


