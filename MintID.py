# Interactive Flowchart: Mint Identification
# Emmett Wald
# this flowchart helps the user distinguish between
# several common varieties of garden mints

"""Key includes spearmint, peppermint, chocolate mint, lemon balm, bee balm,
catnip, basil, rosemary, oregano, thyme, and sage."""

# Define your functions here
def intro():
  print("""
MINT IDENTIFICATION

Perhaps you got a mint plant as a gift and don't
know what sort it is. Or perhaps you lost the tag.
Or maybe it's growing rogue in your yard and you'd
like to figure out what the heck it is.

This interactive dichotomous key will help you
determine what type of mint you have (if, indeed,
it is some type of mint.""")
  pause()
  print("""If you are unfamiliar with botany terminology, you
may find https://gobotany.newenglandwild.org/glossary/a/
a useful resource.""")
  pause()
  
  print("""First, let's make sure that the plant you're
looking at is actually a mint. Does the plant have:""")
  print("""1) a square or rounded stem; opposite
   branching and leaf arrangement; simple, pinnate
   leaves; a strong fragrance when crushed; and,
   if flowers are present, small, irregular,
   bilaterally symmetrical flowers, often purple,
   pink, or white; or""")
  print("""2) alternate branching, no fragrance, or leaves or
   flowers other than as described above?""")
  return makeChoice(2)
  
def pause():
  print("\nHit ENTER to continue.")
  input()

def makeChoice(numChoices):
  choice = 0
  while choice < 1 or choice > numChoices:
    print()
    choice = input("> ")
    try:
      choice = int(choice)
    except:
      print("\nThat's not a number.")
      choice = 0
  print()
  return choice

def itsAMint():
  print("Okay, seems like it's probably a mint.")
  pause()
  print("So, is the stem:")
  print("1) Square, or")
  print("2) Round?")
  return makeChoice(2)

def notAMint():
  print("""Woops, I don't think you're looking at a mint
plant. Don't eat it unless you figure out what it
*is* and it's edible! If you live in the
Northeastern US, you can check out 
https://gobotany.newenglandwild.org/ to help
figure it out.""")

def squareStem():
  return

def roundStem():
  return

def entire():
  return
  
def toothed():
  return

# Your program starts here
choice = intro()
if choice == 1:
  choice = itsAMint()
  if choice == 1:
    entire()
  elif choice == 2:
    toothed()
elif choice == 2:
  notAMint()
