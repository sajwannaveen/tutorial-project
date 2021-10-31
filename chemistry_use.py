import os
from Chemistry12Funtion import *
from main_funtion import *
import question1
#from question1 import question
import os
from Chemistry12Funtion import *
from main_funtion import *
import question1
#from question1 import question
def Chemistry():
    while(1==1):
        print("``````````")
        print("MENU")
        print("```````````````````````````````````````````````````````````````````````````````")
        print("1)Solution Chapter from Class 12th NCERT tutorial")
        print("2)Solution Chapter multiple choice question")
        print("3)Summary of solution")
        print("0)Exit")
        print("```````````````````````````````````````````````````````````````````````````````")
        ch=input("Enter your choice from menu")
        if(ch=='3'):
            writespeak("""A solution is a homogeneous mixture of two or more substances. Solutions are classified as solid, liquid and gaseous solutions. The concentration of a solution is expressed in terms of mole fraction, molarity, molality and in percentages. The dissolution of a gas in a liquid is governed by Henry’s law, according to which, at a given temperature, the solubility of a gas in a liquid is directly proportional to the partial pressure of the gas. The vapour pressure of the solvent is lowered by the presence of a non-volatile solute in the solution and this lowering of vapour pressure of the solvent is governed by Raoult’s law, according to which the relative lowering of vapour pressure of the solvent over a solution is equal to the mole fraction of a non-volatile solute present in the solution. However, in a binary liquid solution, if both the components of the solution are volatile then another form of Raoult’s law is used. Mathematically, this form of the Raoult’s law is stated as:
            ==>ptotal=(p01*X1)+(p02*X2)
Solutions which obey Raoult’s law over the entire range of concentration are called ideal solutions. Two types of deviations from Raoult’s law, called positive and negative deviations are observed. Azeotropes arise due to very large deviations from Raoult’s law.
The properties of solutions which depend on the number of solute particles and are independent of their chemical identity are called colligative properties. These are lowering of vapour pressure, elevation of boiling point, depression of freezing point and osmotic pressure. The process of osmosis can be reversed if a pressure higher than the osmotic pressure is applied to the solution. Colligative properties have been used to determine the molar mass of solutes. Solutes which dissociate in solution exhibit molar mass lower than the actual molar mass and those which associate show higher molar mass than their actual values.
Quantitatively, the extent to which a solute is dissociated or associated can be expressed by van’t Hoff factor i. This factor has been defined as ratio of normal molar mass to experimentally determined molar mass or as the ratio of observed colligative property to the calculated colligative property.""")
            input("Press enter:\t ")
            os.system("cls")
        elif(ch=='2'):
            question1.question()
        elif(ch=='0'):
            exit()
        elif(ch not in "1230"):
            print("Enter only from menu")
        elif(ch=='1'):
            def main():
                os.system("cls")
                print("  *********************************************************************************")
                print("                                     Solution                                                          ")
                print("  *********************************************************************************")
            main()
            #############################################################################################################
            #                                                                                                   First Page
            #############################################################################################################
            print("    Expression for contiontration of solution")
            print("    ......................................................................")
            print("        a)Mass percentage :-")
            solution.expression_for_contiontration.MassPercentage("          ");Nsec(2)
            print("        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("        b)Volume percentage :-")
            solution.expression_for_contiontration.VolumePercentage("          ");Nsec(2)
            print("        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("        c)Mass by volume :-")
            solution.expression_for_contiontration.MassByVolume("          ");Nsec(2)
            print("        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("        d)Part per million :-")
            solution.expression_for_contiontration.PartPerMillion("          ");Nsec(2)
            print("        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("        e)Mole fraction :-")
            solution.expression_for_contiontration.MoleFraction("          ");Nsec(2)
            print("        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("        f)Molarity :-")
            solution.expression_for_contiontration.Molarity("          ");Nsec(2)
            print("        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("        g)Molalty :-")
            solution.expression_for_contiontration.Molality("          ");Nsec(2)
                        print("        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("        b)Volume percentage :-")
            solution.expression_for_contiontration.VolumePercentage("          ");Nsec(2)
            print("        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            writespeak("Press enter for going next topic or any character for end the series ")
            a=input()
            if(a!=""):
                os.system("cls")
                Chemistry()
            main()
            #############################################################################################################
            #                                                                                                   second Page
            #############################################################################################################
            print("    Solubility")
            print("    ...........")
            solution.Solubility.main("      ")
            print("      Solubility of solid in liquid")
            print("        Effect of Temprature   :-")
            solution.Solubility.SolubilityOfSolidInLiguid.temprature("          ");Nsec(2)
            print("        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("        Effect of pressure   :-")
            solution.Solubility.SolubilityOfSolidInLiguid.pressure("          ");Nsec(2)
            print("        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("      Solubility of solid in liquid")
            print("        Effect of pressure  :-")
            solution.Solubility.SolubilityofGasInLiguid.pressure("          ");Nsec(2)
            print("        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("        Henry Law  :-")
            solution.Solubility.SolubilityofGasInLiguid.HenryLaw("          ");Nsec(2)
            print("        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("        Application of henry law  :- ")
            solution.Solubility.SolubilityofGasInLiguid.MoleFraction_HenryLawApplication("          ");Nsec(2)
            print("        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("        Effect of low pressure")
            solution.Solubility.SolubilityofGasInLiguid.lowpressure("          ");Nsec(2)
            print("        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            writespeak("Press enter for going next topic or any character for end the series ")
            a=input()
                        print("        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("        b)Volume percentage :-")
            solution.expression_for_contiontration.VolumePercentage("          ");Nsec(2)
            print("        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            if(a!=""):
                os.system("cls")
                Chemistry()
            main()
            #############################################################################################################
            #                                                                                                   third page
            #############################################################################################################
            print("    Vapour pressure of liquid solution")
            print("    ............................")
            print("    Vapour pressure of  liquid and liquid solution")
            solution.VapourPressureofLiquidSolutions.VapourPressureofLiquidLiquidSolutions1("      ")
            solution.VapourPressureofLiquidSolutions.VapourPressureofLiquidLiquidSolutions2("      ");Nsec(2)
            print("       Coclution from this equation  :-")
            solution.VapourPressureofLiquidSolutions.VapourPressureofLiquidLiquidSolutionsconclusions("      ")
            solution.VapourPressureofLiquidSolutions.VapourPressureofLiquidLiquidSolutionsGraph();Nsec(2)
                        print("        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("        b)Volume percentage :-")
            solution.expression_for_contiontration.VolumePercentage("          ");Nsec(2)
            print("        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("    Vapour pressure of solid liquid solution")
            solution.VapourPressureofLiquidSolutions.VapourPressureofSolidLiquidSolutionsconclusions("      ");Nsec(2)
            writespeak("Press enter for going next topic or any character for end the series ")
            a=input()
            if(a!=""):
                os.system("cls")
                Chemistry()
            main()
                        print("        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("        b)Volume percentage :-")
            solution.expression_for_contiontration.VolumePercentage("          ");Nsec(2)
            print("        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            #############################################################################################################
            #                                                                                                   fourth page
            #############################################################################################################
            print("    Type of solution")
            print("    ..................")
            print("    Ideal solution")
            solution.Typesolution.IdealSolution("      ")
            print("      Properties :-")
            solution.Typesolution.IdealSolutionproperties("        ")
            Nsec(1)
            print("    Non-Ideal solution")
            solution.Typesolution.NonIdealSolution("      ")
            print("      Properties :-")
            solution.Typesolution.NonIdealSolutionproperties("        ")
            writespeak("Press enter for going next topic or any character for end the series ")
            a=input()
            if(a!=""):
                os.system("cls")
                Chemistry()
            main()
            #############################################################################################################
            #                                                                                                   fivth page
            #############################################################################################################
            print("    Colligative Properties of solution")
            print("    ..................................")
            print("    Colligative properties  :-")
            solution.ColligativeProperties.main("      ");Nsec(2)
            print("    Relative Lowering of Vapour Pressure  :-")
            solution.ColligativeProperties.RelativeLoweringofVapourPressure("      ");Nsec(2)
            print("    Elevation of Boiling Point  :-")
            solution.ColligativeProperties.ElevationofBoilingPoint("      ");Nsec(2)
            print("    Depression of Freezing Point  :-")
            solution.ColligativeProperties.DepressionofFreezingPoint("      ");Nsec(2)
            print("    OsmoticPressure")
            solution.ColligativeProperties.OsmoticPressure("      ");Nsec(2)
            writespeak("Press enter for going next topic or any character for end the series ")
            a=input()
            if(a!=""):
                os.system("cls")
                Chemistry()
            main()
            #############################################################################################################
            #                                                                                                   sisth page
            #############################################################################################################
            print("    Abnormal Molar Masses")
            print("    ..........................\n")
            print("    Abnormal mass:-",end="")
            solution.AbnormalMolarMasses("      ")
            writespeak("Press enter for going next topic or any character for end the series ")
            a=input()
            if(a!=""):
                os.system("cls")
                Chemistry()
            main()
            #############################################################################################################
            #                                                                                                   bonus page
            #############################################################################################################
            print("    This is bonus education related to this topic")
            print("\n","    brownian motion")
            brownianmotion("    ")
            main()
            brownianmotion2("    ")
            os.system("cls")
