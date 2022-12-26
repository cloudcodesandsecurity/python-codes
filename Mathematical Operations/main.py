import operator


image = """                                                                                                                                                          
        CCCCCCCCCCCCC                lllllll                                    lllllll                         tttt                                                  
     CCC::::::::::::C                l:::::l                                    l:::::l                      ttt:::t                                                  
   CC:::::::::::::::C                l:::::l                                    l:::::l                      t:::::t                                                  
  C:::::CCCCCCCC::::C                l:::::l                                    l:::::l                      t:::::t                                                  
 C:::::C       CCCCCC aaaaaaaaaaaaa   l::::l    cccccccccccccccuuuuuu    uuuuuu  l::::l  aaaaaaaaaaaaa ttttttt:::::ttttttt      ooooooooooo  rrrrr   rrrrrrrrr        
C:::::C               a::::::::::::a  l::::l  cc:::::::::::::::u::::u    u::::u  l::::l  a::::::::::::at:::::::::::::::::t    oo:::::::::::oor::::rrr:::::::::r       
C:::::C               aaaaaaaaa:::::a l::::l c:::::::::::::::::u::::u    u::::u  l::::l  aaaaaaaaa:::::t:::::::::::::::::t   o:::::::::::::::r:::::::::::::::::r      
C:::::C                        a::::a l::::lc:::::::cccccc:::::u::::u    u::::u  l::::l           a::::tttttt:::::::tttttt   o:::::ooooo:::::rr::::::rrrrr::::::r     
C:::::C                 aaaaaaa:::::a l::::lc::::::c     ccccccu::::u    u::::u  l::::l    aaaaaaa:::::a     t:::::t         o::::o     o::::or:::::r     r:::::r     
C:::::C               aa::::::::::::a l::::lc:::::c            u::::u    u::::u  l::::l  aa::::::::::::a     t:::::t         o::::o     o::::or:::::r     rrrrrrr     
C:::::C              a::::aaaa::::::a l::::lc:::::c            u::::u    u::::u  l::::l a::::aaaa::::::a     t:::::t         o::::o     o::::or:::::r                 
 C:::::C       CCCCCa::::a    a:::::a l::::lc::::::c     ccccccu:::::uuuu:::::u  l::::la::::a    a:::::a     t:::::t    ttttto::::o     o::::or:::::r                 
  C:::::CCCCCCCC::::a::::a    a:::::al::::::c:::::::cccccc:::::u:::::::::::::::ul::::::a::::a    a:::::a     t::::::tttt:::::o:::::ooooo:::::or:::::r                 
   CC:::::::::::::::a:::::aaaa::::::al::::::lc:::::::::::::::::cu:::::::::::::::l::::::a:::::aaaa::::::a     tt::::::::::::::o:::::::::::::::or:::::r                 
     CCC::::::::::::Ca::::::::::aa:::l::::::l cc:::::::::::::::c uu::::::::uu:::l::::::la::::::::::aa:::a      tt:::::::::::ttoo:::::::::::oo r:::::r                 
        CCCCCCCCCCCCC aaaaaaaaaa  aaallllllll   cccccccccccccccc   uuuuuuuu  uuullllllll aaaaaaaaaa  aaaa        ttttttttttt    ooooooooooo   rrrrrrr"""

print(image)

users_first_number = float(input("Type your First number: "))
symbol = input("Enter a calculation symbol for calculation you want to perform: ")
users_second_number = float(input("Type your Second number: "))


operatorlookup = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}
op = operatorlookup.get(symbol)

wrong_result = "Unknown operator"
if op is not None:
    result = op(float(users_first_number), float(users_second_number))
    print(result)
    your_operations = input("Do you want to continue your operations?: ")
    if your_operations == 'yes':
        next_result = 0
        next_result2 = 0

        next_symbol = input("Enter a calculation symbol for calculation you want to perform: ")
        users_other_number = float(input("Type your other number: "))
        op2 = operatorlookup.get(next_symbol)
        next_result = op2(float(result), float(users_other_number))
        print(next_result)

    else:
        print("Thank you for trying out Calculator 1.0")


else:
    print("You have entered a wrong operation symbol: " + str(wrong_result))

