
#strip() function
# def custom_strip(text, chars=None):
#     # If no characters are provided, default to whitespace
#     if chars is None or chars == " ":
#         chars = " "  

#     # Remove leading characters (ignore this loop for Custome_lstrip)
#     start_index = 0     
#     while start_index < len(text) and text[start_index] == chars: 
#         start_index += 1

#     # Remove trailing characters(ignore this loop for the Custom_lstrip())
#     end_index = len(text) - 1
#     while end_index >= start_index and text[end_index] == chars:
#         end_index -= 1

#     # Return the trimmed string
#     return text[start_index:end_index + 1]

# # Get input from user
# str = input("Enter a string: ")
# space = input("Enter characters to strip (press Enter to strip whitespace): ")

# # Call to function
# stripped_string = custom_strip(str, space)
    
# print("Original string:", custom_strip(str))




#SPLIT CUSTOME METHOD

# def Customsplit(str,splitby=None):
#     if splitby== None or splitby== " ":
#         splitby=" "
    
    
#     result= []
#     current=""
    
#     for i in str:
#         if i == splitby :
#             result.append(current)
#             current= ""
#         else:
#             current+=i
    
#     result.append(current)
#     return result
    
# str1= input("enter the string:")
# splitby =input("enter the symbol for split")


# str1 = Customsplit(str1,splitby)
# print(str1)


#3. REPLACE() IN PYTHON 
##replace(): it will replace the string with another string 

# def Custom_replace(str,chartorep,alternative):
    
#     result=""
#     for i in str:
#         if i == chartorep: #whenever the ith index value gets equal to the chartorep then we put the alternative in place of it 
#             result+=alternative
#         else:
#             result += i #otherwise we simply put the ith value in the result 
    
#     return result #returning the result 
    
    

# str=input("enter the string: ")
# chartorep =input("enter the character  to rep:")
# alternative =input("enter the character  you want as replacement: ")

# str = Custom_replace(str,chartorep,alternative)
# print(str)
 


#Lower to Uppercase
# def Uppercase(str8):
#     char1 = "abcdefghijklmnopqrstuvwxyz"
#     char2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
#     result=""
    
#     for i in str8:
#         if i in char1:  #agar i mera char1 hai to ya uski index value nikalega char1 ke and same index value ka char2[i] ko put krdega result mai
#             index = char1.index(i)
#             result += char2[index]
#         else:
#             result+=i #keep other char unchanged
            
#     return result
    
    
# str8="abc"
# str8=Uppercase(str8)
# print(str8)

#lower TO UPPER
def Uppercase(str8):
    char1 = "abcdefghijklmnopqrstuvwxyz"
    char2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    result=""
    
    for i in str8:
        if i in char2: 
            index = char2.index(i)
            result += char1[index]
        else:
            result+=i #keep other char unchanged
            
    return result
    
    
str8="ABC"
str8=Uppercase(str8)
print(str8)