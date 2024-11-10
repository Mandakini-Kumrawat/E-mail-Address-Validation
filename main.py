# Validate E-mail Address ------------------>

email = input ( " Enter Your Email : " )
space , upper , special_char = 0 , 0 , 0

if len ( email ) >= 6 :
    if email [ 0 ].isalpha () :
        if ( "@" in email ) and ( email.count ( "@" ) == 1 ) :
            if ( email [ -3 ] == "." ) ^ ( email [ -4 ] == "." ) :
                for i in email :
                    if i == i.isspace () :
                        space = 1
                    elif i.isalpha () :
                        if i == i.upper () :
                            upper == 1
                    elif i.isdigit () :
                        continue
                    elif i == "_" or i == "." or i == "@" :
                        continue
                    else :
                        special_char = 1
                if space == 1 or upper == 1 or special_char == 1 :
                    print ( " 5 - Invalid Email ! ( A Valid Email Must Not Have Any Space(s) Or Upper Case Letter(s) or Special Charachter(s). ) " )
                print ( " Weldone ! " )
            else :
                print ( " 4 - Invalid Email ! ( A Valid Email Must Have '.' At The Right Place. )" )
        else :
            print ( " 3 - Invalid Email ! ( A Valid Email Must Have '@' atleast Once In It. ) " )
    else :
        print ( " 2 - Invalid Email ! ( A Valid Email Must Start With An Alphabet. ) " )
else :
    print ( " 1 - Invalid Email ! ( A valid Email Must Contain Atleast 6 Characters. ) " )


