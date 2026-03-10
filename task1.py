Good = r"""    EeeiiiiiEEiiiii.....
       \|/
        n______     .....iiiiiEEiiiieeEE
       :~;     :                  \|/
-----;``~'  +  ;------------ ______n --------------------------------
     `-@-----@-=            :     :~:
=========================== ;  +  '~``; =============================
                            =-@-----@-'
jgs------------------------------------------------------------------
"""
bad = r""""""
# Task 1
torch_lit = True

if torch_lit:
    outcome = "Flicker: The torch lights the damp walls and reveals a path forward."
    print(outcome)
    print(Good)
else:
    outcome = "Doom: Darkness swallows the room and you stumble into the abyss."
    print(outcome)
    print(bad)