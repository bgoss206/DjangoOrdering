from main.models import Sundry
from random import randint 

sundryStrings = """INTERTAPE BLONDE 1-1/2" TAPE
3M 2020 ORANGE  1-1/2" TAPE
3M 2090  BLUE 1-1/2" TAPE
DUCT TAPE GRAY 2"
CAUTION / DANGER TAPE
SHRINK WRAP TAPE
GREEN HM PAPER 12"
GREEN HM PAPER 18"
FLOOR PAPER 35"
FLOOR PAPER 48"
3M APF HM FILM 48"
3M APF HM FILM 72"
3M APF HM FILM 99"
9x400 PLASTIC ALL PRO
12x400 PLASTIC ALL PRO
4x1/2" STRIPE WEENIE ROLLER
4x1/2" PINK WEENIE ROLLER
4" FOAM ROLLER
4" MOHAIR BLEND WEENIE
6.5x3/8" WEENIE COVER
6.5" STRIPE 
4x1" JUMBO COATER
3x1" JUMBO COATER
9x1/2" ROLLER COVER
9x3/4" ROLLER COVER
9" MOHAIR COVER
18x1/2" ROLLER COVER
18x3/4" ROLLER COVER
18" ROLLER FRAME
2" CHIP BRUSH
9" SCREENS/GRIDS
SPRAY SOCK
5 GAL STRAINER BAGS
TACK CLOTH
1 LB RAGS
6.5x1/4 WHITE WOVEN
18x3/8 CS SOFT WOVEN
9x1/4 CS SOFT WOVEN
PREFILTER
FILTER CARTRIDGE - YELLOW
FILTER CARTRIDGE - PURPLE
SAFETY GLASSES
DUST CUP
GLOVES - LG
GLOVES - XL
THICKSTER GLOVES
SHOE COVERS
TYVEX SUIT
SANDING SPONGE
SAND PAPER <220 GRIT
SAND PAPER 220 GRIT
SAND PAPER 180 GRIT
SAND PAPER 150 GRIT
SAND PAPER 120 GRIT 
SAND PAPER >120 GRIT
SPRAY ADHESIVE
ALL PRO QUICK CAULK
ALL PRO STRETCH CAULK
FINISH MAX SEALANT
POWER HOUSE BLACK CAULK
WHITE LIGHTNING QUICK CAULK
ELMERS WOOD FILLER
CRAWFORD SPACKLE
LIGHTWEIGHT SPACKLE
ONETIME SPACKLE
HOMAX WB TEXTURE 
HOMAX SOLVENT TEXTURE
BONDO
RED BONDO
PROBLOCK AEROSOL PRIMER
CONTRACTOR TRASH BAG
LIFT OFF
SIMPLE GREEN
THINNER/REDUCER (SPECIFY)
9x3/16 CS SOFT WOVEN
9X3/8 CS SOFT WOVEN"""


listOfSundries = sundryStrings.split('\n')


for i in listOfSundries: 
    s = Sundry(name=i, quantity_available=randint(0, 100))
    s.save()