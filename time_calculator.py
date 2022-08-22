def arithmetic_arranger(a , b=False) :

  line_1=[]
  line_2=[]
  dash_list=[]
  line_4=[]
  if len(a) > 5 :
    return "Error: Too many problems"
  for i in range(len(a)) :
#globals()[f"problem{i}"] = a[i]
   problem= a[i].split()
   if problem[0].isdigit() and problem[2].isdigit() : 
     if len(problem[0]) <5 and len(problem[2]) < 5 :
       if problem[1]== '+' or problem[1]== '-' :
         max_number= max(len(problem[0] ), len(problem[2]))

         max_length = max_number + 2
         right_aligned_number_1=problem[0].rjust(max_length)+"   "
         right_aligned_number_2=problem[2].rjust(max_length-2)
         x_2=problem[1] + " " + right_aligned_number_2 + "   "
         line_1.append(right_aligned_number_1)
         line_2.append(x_2)
         dash_1=''
         for i in range(max_length) :
           dash_1+='-'
         
         dash_2=dash_1+"   "
           
        
         dash_list.append(dash_2)
         if problem[1] == '+' :
           final=str(int(problem[0])+ int(problem[2])).rjust(max_length)+"   "
           line_4.append(final)
         else:
          final=str(int(problem[0]) - int(problem[2])).rjust(max_length)+"   "
          line_4.append(final)


                 
         #print(right_aligned_number_1)
         #print(problem[1] + " " + right_aligned_number_2)
         #print(dash_1)



       else :
           return "Error: Operator must be '+' or '-'"
           break
       
     else : 
       return "Error: Numbers cannot be more than four digits"
       break
   else : 
       return "Error: Numbers must only contain digits."
       break
  print(*line_1)
  print(*line_2)
  print(*dash_list)
  if b :
    print(*line_4)
  

  
