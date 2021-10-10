from main_funtion import *
class solution:
    class expression_for_contiontration:
        def MassPercentage(space):
            writespeak(space+"The mass percentage of a compound of a solution is defined as:")
            print(space,"Mass percentage")
            print(space,"-------------------------------X100 ",)
            print(space,"Total mass of the solution")
            writespeak(space+"it means if we say 10%glucose in water by mass means 100 gram of water contain 10gm glucose")
        def VolumePercentage(space):
            writespeak(space+"The volume percentage of a compound of a solution is defined as:")
            print(space,"Mass percentage")
            print(space,"------------------------------- X100 ",)
            print(space,"Total mass of the solution")
            writespeak(space+"it means if we say 10% (v/v)glucose in water  means 100 ml of water contain 10ml glucose")
        def MassByVolume(space):
            writespeak(space+"The Mass by volume of a compound is another unit in which is commonly used in medicine and pharmacy is mass by volume percantage.")
            print(space,"Mass percentage")
            print(space,"-------------------------------X100 ",)
            print(space,"Total volume of the solution")
            writespeak(space+"it means if we say 10% (m/v)glucose in water  means 100 ml of water contain 10gram glucose")
        def PartPerMillion(space):
            writespeak(space+"When a solute is present in trace quantitie,it is convenient to express concentration in part per million .it is defined as :-")
            print(space,"Number of part of the component")
            print(space,"------------------------------- X1000000 ",)
            print(space,"Total number of part of all components of the solution")
            writespeak(space+"A litre of the sea water (which weight 1030gram) contain 0.006gram of dissolved oxygen (O2).Such a small contiontration is expressed by part per million")
            print(space,"Commonly it's expressed in µg/mL or ppm")
        def MoleFraction(space):
            writespeak(space+"Commonly used symbol for mole fraction is X. It is defined as:-")
            writespeak("\n"+space+"mole fraction of a component a is:-")
            print(space,"Number of part of the component a")
            print(space,"------------------------------------",)
            print(space,"Total number of mole of all the components")            
            writespeak(space+"Sum of mole fraction of all component of a solution is equal to 1")
            print(space,"∑Xi=1")
        def Molarity(space):
            writespeak(space+"it is defined as number of mole of solute dissolved in one litre of solution(or one cubic decimetere)of the solution")
            print(space,"Mole of solute")
            print(space,"------------------------------------",)
            print(space,"Volume of solution in litre")
            writespeak(space+"0.25M solution of NaOH in water means ,1 litre of solution contain 0.25mole of NaOH or 9.99925gram (molar mass of NaOH is 39.997gram)")
        def Molality(space):
            writespeak(space+"it is defined as number of mole of solute dissolved in one kilogram of solvent")
            print(space,"Mole of solute")
            print(space,"------------------------------------",)
            print(space,"Weight of solvent in kilogram")
            writespeak(space+"0.25m solution of NaOH in water means ,1 kilogram of water contain 0.25mole of NaOH or 9.99925gram (molar mass of NaOH is 39.997gram)")
    class Solubility:
        def main(space):
            writespeak(space+"Solubility of the substance is its maximium amount that can br dissoled in a specified amount of solvent.")
            writespeak(space+"Solubility depend's upon temprature ,pressure and nature of solute,sovent ")
        class SolubilityOfSolidInLiguid:
            def temprature(space):
                writespeak(space+"Process of dissolving of is endothermic reaction (chande H>0) so due to Le Chetelies Principla. we conclude  :-")
                writespeak(space+"Solubility of solid in liquid increase with rise in temprature and decrease with decrease in temprature")
            def pressure(space):
                writespeak(space+"Solubiliy of solid in liquid is independent of pressure ")
        class SolubilityofGasInLiguid:
            def pressure(space):
                writespeak(space+"Solubility of gas in liquid increase with increase in pressure and decrease with decrease in temprature")
            def HenryLaw(space):
                import matplotlib.pyplot as ankit
                ankit.title("Experimental result for the solubility of HCl gas in cyclohexane at 293k or  19.85°C or  67.73°F .The slope of the line is the Henry's Law constant K")
                writespeak(space+"The partial pressure of gas in vapour phase(p) is proportional to the mole fraction of the gas(X) in solution")
                ankit.ylabel("Partial pressure of Hcl\torr")
                ankit.xlabel("Mole fraction of HCl gas in Cyclohexane at 293k or  19.85°C or  67.73°F")
                print(space,"    P directly propotional to X")
                print(space,"→ P=KX") 
                print(space,"K is henry's law constant")
                ankit.plot([x/1000 for x in range(1000)],[x*13 for x in range(1000)],"p:",color="red")
                ankit.show()
            def MoleFraction_HenryLawApplication(space):
                writespeak(space+"Henry’s law finds several applications in industry and explains some biological phenomena. Notable among these are:")
                writespeak(space+"1)To increase the solubility of CO 2 in soft drinks and soda water, the bottle is sealed under high pressure.")
                writespeak(space+"2)Scuba divers must cope with high concentrations of dissolved gases while breathing air at high pressure underwater. Increased pressure increases the solubility of atmospheric gases in blood. When thedivers come towards surface, the pressure gradually decreases. This releases the dissolved gases and leads to the formation of bubbles of nitrogen in the blood. This blocks capillaries and creates a medical condition known as bends, which are painful and dangerous to life.To avoid bends, as well as, the toxic effects of high concentrations of nitrogen in the blood, the tanks used by scuba divers are filled with air diluted with helium (11.7% helium, 56.2% nitrogen and 32.1% oxygen)")
                writespeak(space+"3)At high altitudes the partial pressure of oxygen is less than that at the ground level. This leads to low concentrations of oxygen in the blood and tissues of people living at high altitudes or climbers. Low blood oxygen causes climbers to become weak and unable to think clearly, symptoms of a condition known as anoxia.")
            def lowpressure(space):
                 writespeak(space+"At high altitudes the partial pressure of oxygen is less than that at the ground level. This leads to low concentrations of oxygen in the blood and tissues of people living at high altitudes or climbers. Low blood oxygen causes climbers to become weak and unable to think clearly, symptoms of a condition known as anoxia.")
    class VapourPressureofLiquidSolutions:
        def VapourPressureofLiquidLiquidSolutions1(space):
            writespeak(space+"Let us consider a binary solution of two volatile liquids and denote the two components as 1 and 2. When taken in a closed vessel, both the components would evaporate and eventually an equilibrium would be established between vapour phase and the liquid phase. Let the total vapour pressure at this stage be p total  and p 1 and p 2 be the partial vapour pressures of the two components 1 and 2 respectively. These partial pressures are related to the mole fractions x1 and x2 of the two components 1 and 2 respectively.")
        def VapourPressureofLiquidLiquidSolutions2(space):
            writespeak(space+"The relationship is known as the Raoult’s law which states that for a solution of volatile liquids,the partial vapour pressure of each component in the solution is directly proportional to its mole fraction.")
            print(space,"    p¹ directly propotional to X¹")
            print(space,"→ p¹=p0¹*X¹") 
            print(space,"p0¹ is the vapour pressure of pure component 1 at the same temperature.")
            writespeak(space+"Similarly, for component 2")
            print(space,"    p² directly propotional to X¹")
            print(space,"→ p²=p0²*X²") 
            print(space,"p0² is the vapour pressure of pure component 1 at the same temperature.")
            writespeak("According to Dalton’s law of partial pressures, the total pressure (p¹²) over the solution phase in the container will be the sum of the partial pressures of the components of the solution and is given as:")
            print("                       →p¹²=p¹+p²")
            Nsec(2)
            print("                       →p¹²=(p0¹*X¹)+(p0²*X²)")
            Nsec(2)
            print("                       →p¹²=(p0¹*(1-X²))+(p0²*X²)")
            Nsec(2)
            print("                       →p¹²=p0¹-(p0¹*X²)+(p0²*X²)")
            Nsec(2)
            print("                       →p¹²=p0¹+(p0²-p0¹)X²")
        def VapourPressureofLiquidLiquidSolutionsconclusions(space):
            writespeak(space+"(i)Total vapour pressure over the solution can be related to the mole fraction of any one component.")
            writespeak(space+"(ii) Total vapour pressure over the solution varies linearly with the mole fraction of component 2.")
            writespeak(space+"(iii)  Depending on the vapour pressures of the pure components 1 and 2, total vapour pressure over the solution decreases or increases with the increase of the mole fraction of component 1.")
        def VapourPressureofLiquidLiquidSolutionsGraph():
            import matplotlib.pyplot as ankit
            PCHCl3=200;PCH2Cl3=415
            xCHCl3=[x/100 for x in range(0,105,5)]
            xCH2Cl3=[1-x for x in xCHCl3]
            GCHCl3=[200*x for x in xCHCl3]
            GCH2Cl3=[415*x for x in xCH2Cl3]
            GTotalpressure=[GCHCl3[x]+GCH2Cl3[x] for x in range(len(xCHCl3))]
            ankit.xlabel("mole fraction of CHCl3")
            ankit.ylabel("Pressure")
            ankit.plot(xCHCl3,GCHCl3,"p--",color="green",label="Mole fraction and partial pressure of CHCl3")
            ankit.plot(xCHCl3,GCH2Cl3,"p-.",color="cyan",label="Mole fraction and partial pressure of CH2Cl3")
            ankit.plot([x/100 for x in range(0,105,5)],GTotalpressure,"p-",color="brown",label="Total Vapour Pressure of solution",linewidth=5)
            ankit.legend()
            ankit.show()
        def VapourPressureofSolidLiquidSolutionsconclusions(space):
            writespeak(space+"In a binary solution, let us denote the solvent by 1 and solute by 2. When the solute is non-volatile, only the solvent molecules are present in vapour phase and contribute to vapour pressure. Let p¹  be the vapour pressure of the solvent, X¹ be its mole fraction, p0¹ be its vapour pressure in the pure state. Then according to Raoult’s law")
            print(space+"    p¹ directly propotional to X¹");
            print(space+"    p² directly propotional to X²");
    class Typesolution:
            def IdealSolution(space):
                writespeak(space+"The solutions which obey Raoult’s law over the entire range of concentration are known as ideal solutions.")
            def IdealSolutionproperties(space):
                writespeak(space+"The enthalpy of mixing of the pure components to form the solution is zero and the volume of mixing is also zero")
                print(space,"→  Δmix H = 0")
                print(space,"→  Δmix V = 0")
                print(space+"""It means that no heat is absorbed or evolved when the components
are mixed. Also, the volume of solution would be equal to the sum of
volumes of the two components. At molecular level, ideal behaviour of
the solutions can be explained by considering two components A and
B. In pure components, the intermolecular attractive interactions will
be of types A-A and B-B, whereas in the binary solutions in addition
to these two interactions, A-B type of interactions will also be present.
If the intermolecular attractive forces between the A-A and B-B are
nearly equal to those between A-B, this leads to the formation of ideal
solution. A perfectly ideal solution is rare but some solutions are nearly
ideal in behaviour. Solution of n-hexane and n-heptane, bromoethane
and chloroethane, benzene and toluene, etc. fall into this category.""")
            def NonIdealSolution(space):
                writespeak(space+"The solutions which do not obey Raoult’s law over the entire range of concentration are known as Non-ideal solutions.")
            def NonIdealSolutionproperties(space):
                writespeak(space+"The enthalpy of mixing of the pure components to form the solution is zero and the volume of mixing is also zero")
                print(space,"→  Δmix H = 0")
                print(space,"→  Δmix V = 0")
    class ColligativeProperties:
        def main(space):
            writespeak(space+"All these properties depend on the number of solute particles irrespective of their nature relative to the total number of particles present in the solution. Such properties are called colligative properties")
        def  RelativeLoweringofVapourPressure(space):
            writespeak(space+"The vapour pressure of a solvent is lowered when a non-volatile solute is dissolved in it to form a solution. The vapour pressure lowering relative to pure solvent is , which is proportional to the mole fraction of solute.")
            print(space,"\t       p²=p0²*X²")
            print(space,"\t→\tΔp²=p0²-p²=p0²-p0²*X²=p0²X¹")
            print(space,"\t→\t Δp²/Δp0²=X¹")
        def ElevationofBoilingPoint(space):
            writespeak(space+"Boiling-point elevation describes the phenomenon that the boiling point of a liquid (a solvent) will be higher when another compound is added, meaning that a solution has a higher boiling point than a pure solvent. This happens whenever a non-volatile solute, such as a salt, is added to a pure solvent, such as water.")
            writespeak(space+"Experiments have shown that for dilute solutions the elevation of boiling point (ΔT b ) is directly proportional to the molal concentration of the solute in a solution. Thus")
            print(space,"\tΔTb directly propotional to m")
            print(space,"\t→ΔTb= Km")
            writespeak(space+" Kb    is Boiling Point Elevation Constant or Molal Elevation Constant (Ebullioscopic Constant).")
            import matplotlib.pyplot as ankit
            ankit.xlabel("Boiling point of sucrose solution")
            ankit.ylabel("Molality of sucrose")
            ankit.plot([x for x in range(10)],[100+(x/2) for x in range(10)],color="black")
            ankit.show()
        def  DepressionofFreezingPoint(space):
            writespeak(space+" The freezing point of a solution is less than the freezing point of the pure solvent. This means that a solution must be cooled to a lower temperature than the pure solvent in order for freezing to occur. The freezing point of the solvent in a solution changes as the concentration of the solute in the solution changes ( but it does not depend on the identity of either the solvent or the solute(s) particles (kind, size or charge) in the solution).")
            writespeak(space+"Experiments have shown that for dilute solutions the Depression of Freezing Point (ΔTf ) is directly proportional to the molal concentration of the solute in a solution. Thus")
            print(space,"\t→ΔTb directly propotional to m")
            print(space,"\t→ΔTb= Kbm")
            writespeak(space+" K f is Freezing Point Depression Constant or Molal Depression Constant ( Cryoscopic Constant ).")
            import matplotlib.pyplot as ankit
            ankit.xlabel("Frezing point of sucrose solution")
            ankit.ylabel("Molality of sucrose")
            ankit.plot([x for x in range(10)],[-2*x for x in range(10)],color="black")
            ankit.show()
        def OsmoticPressure(space):
            writespeak(space+"Osmotic pressure is the minimum pressure which needs to be applied to a solution to prevent the inward flow of its pure solvent across a semipermeable membrane. It is also defined as the measure of the tendency of a solution to take in pure solvent by osmosis.")
            writespeak(space+"This process of flow of the solvent is called osmosis.")
            writespeak(space+"osmotic pressure is proportional to the molarity, C of the solution at a given temperature T.")
            print(space,"    →ð = C R T");Nsec(1)
            print(space,"    →ð = (N²/V) R T");Nsec(1)
            print(space,"    →ðV = N²RT");Nsec(1)
            writespeak(space+"Two solutions having same osmotic pressure at a given temperature are called isotonic solutions")
    def AbnormalMolarMasses(space):
        writespeak(space+"Molar masses that are lower or higher than expected values when calculated (generally using colligative properties) are called abnormal molar masses. Abnormal molar masses depends upon the total number of moles particles either after dissociation or association of solute molecules in solvent or solution.")
        writespeak(space+"The van 't Hoff factor is the ratio between the actual concentration of particles produced when the substance is dissolved and the concentration of a substance as calculated from its mass. For most non-electrolytes dissolved in water, the van 't Hoff factor is essentially 1")
        print(space,"Von't Hoff factor (i) =")
        print(space,"   Normal molar mass")
        print(space,"=-------------------------------")
        print(space,"   Abnormal molar mass\n")
        print(space,"   Observed colligative property")
        print(space,"=-------------------------------")
        print(space,"   Calculated colligative property\n")
        print(space,"   Total number of moles of particles after association/dissociation")
        print(space,"=-------------------------------")
        print(space,"   Number of moles of particles before association/dissociation")
        print("\n")
        writespeak(space+"Von't Hoff factor of NaCl,KCl,MgSO4 is 2 ,CaCl2 is 3,and glucose is 1")
        print(space,"Elevation of boiling point,    ΔTb= iKbm")
        print(space,"Depression of Freezing point, ΔTf = iKfm")
        print(space,"Osmotic pressure of solution, ð = iN²RT/V")
        import matplotlib.pyplot as ankit
        ankit.title("Von't Hoff factor NaCl,KCl,MgSO4,K2SO4")
        ankit.plot(["NaCl","KCl","MgSO4","K2SO4"],[1.87,1.85,1.21,2.32],"p:",label="Von't Hoff factor when 0.1 m is associated/dissociated ")
        ankit.plot(["NaCl","KCl","MgSO4","K2SO4"],[1.94,1.94,1.53,2.7],"p-.",label="Von't Hoff factor when 0.01 m is associated/dissociated ")
        ankit.plot(["NaCl","KCl","MgSO4","K2SO4"],[1.97,1.98,1.82,2.84],"p--",label="Von't Hoff factor when 0.001 m is associated/dissociated ")
        ankit.plot(["NaCl","KCl","MgSO4","K2SO4"],[2,2,2,3],label="van’t Hoff Factor i for complete dissociation of solute",linewidth=2)
        ankit.legend()
        ankit.show()
def brownianmotion(space):
    global pygame
    import pygame,random
    pygame.init()
    screen = pygame.display.set_mode((640, 480), 0, 32)
    pygame.draw.circle(screen, [255,0,0], (200,200),10)
    def cir(i):
        for x in i:
            pygame.draw.circle(screen,[255,255,255],x,5)
            pygame.display.update()
    p=[150,150]
    for x in range(500):
        screen.fill((0, 0, 0))
        l=[]
        for x in range(20):
            l+=[(random.randrange(100,500),random.randrange(100,500))]
        cir(l)
    pygame.quit()
def brownianmotion2(space):
    writespeak(space+"This random motion is known as brownian motion")
    writespeak(space+"Brownian motion is the random movement of particles in a fluid due to their collisions with other atoms or molecules.Brownian motion takes its name from the Scottish botanist Robert Brown, who observed pollen grains moving randomly in water. He described the motion in 1827 but was unable to explain it.")
    
