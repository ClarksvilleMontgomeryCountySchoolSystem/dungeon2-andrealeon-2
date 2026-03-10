
Good = r"""    
              __   
           .-'  '-.       
          /        )                                 
          |  C   o( 
           \       >      
            )  \  /      ..`'
         .-._ / `'      /////     
        / _    \       ( | /
        |/ )    \\     / _,
        / /      |\   / /
       / /       | \ / /
      (  )       /\ ' /
       \ \      (  `-'
        \ \      Y 
        /\ `-.   |
        |(   ^'  |
        \ \\\\  /
         `-    f|
           |   ||
           |   f/
           j   /
           |   )
           |  |
           /  |
           f  |
           \  |
            | |&
           (   `-._,
            -^-----'
"""
bad = r""""""
# Task 3
guard_alert = False

if not guard_alert:
    outcome = "Shadow: You slip past the guard unnoticed."
    print(outcome)
    print(Good)
else:
    outcome = "Doom: The guard spots you and raises the alarm."
    print(outcome)
    print(bad)