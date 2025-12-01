for _ in range(int(input())):
   a,b,c,d = map(int,input().split())
   if [a,b,c,d].count(a)==4:
      print("YES")
   else:
      print("NO")