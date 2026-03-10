
Good = r"""    
      ,    /),
     (( -.((_))  _,)
     ,\`.'_  _`-','
     `.> <> <>  (,-
    ,',    |     `._,)
   ((  )   |,   (`--'
    `'( ) _--_,-.\ SSt
       /,' \( )  `'
      ((    `\
       `

"""
bad = r""""""
# Task 5
escaped = True

if escaped:
    outcome = "Legend: You step into the daylight, free at last."
    print(outcome)
    print(Good)
else:
    outcome = "Doom: The dungeon claims another prisoner."
    print(outcome)
    print(bad)