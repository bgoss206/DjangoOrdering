from main.models import Jobsite
jobsite_string = """ Andrew McNeil
AnnaLee Baglio
Ashley Hutchison
Becky Heistand
Bill &amp; Donna Deck
Bill &amp; Tina Jones
BJC - Mullenix Convenience
BJC - Old Town TI Tacoma
BJC - Operations Bldg
BJC - Pendleton Place
BJC - Wells Mets
BJC- Ridgetop Carwash
BJC- Tree Farm
Bob and Jackie Fojtik
Brown - Manchester
Building 856
Button Chiropractic
Cenningham
Chinook Center
Chinook Norland Trails
CHT Tank
Dan Lewandowski
Diana Snow
Erlands Point Apartment
Evergreen State College
Fort Flagler State Park
Harborside Condos
Hegewald - Lake Home
Hegewald - Primary
Hunt - The Landings
Hunt Ext Repaints- Bangor
Hunt Ext Repaints- Lake Stevens
Hunt- Whidbey Island
Hunt-Keyport
Island Village- Bainbridge Island
Jackson Park Crack Filling
Jennifer Davis
Jennifer Lewis
John Boothby
Kelly Clark (New Home)
King Homes - Forest View
King Homes - OAS Lot 1
King Homes - Orchard
King Homes - Tacoma
King Homes - Zimmerman
Kiwi
Landmark Construction
Lyman Repaint
Lynn Slaughter - Capitol Hill
Manette View Townhomes
Nancy Doll
Nelson - Packard Ln
Nelson - Poulsbo
Nelson - Sunrise
Nelson - Wagner
Nelson - Zanette
Nick Sample (Nicholson Drilling)
Ogun Arslan
OPC
Perkins
R &amp; J B.I. Craftsman
R &amp; J Dipo Remodel
R&amp;J Construction- Belfair Burn
Randy Clark
Rich and Robin Watkyns
Rory Jefferson
Schaerer
SF Kafer - Troon - Gail
SF Kafer Island Lake
SHOP
Starbucks
Steven Kafer
The Preserve Lot 2
TPG - The Meridian
TPG - Vineyard Lane
TRC - Bremerton Renovation
TRC - Holt Residence
TRC-Harborside Garage Line Stripping
Viking Crest Condos
Vince Holt """


jobsite_list = jobsite_string.split('\n')


for name in jobsite_list:
    j = Jobsite(name=name)
    j.save()