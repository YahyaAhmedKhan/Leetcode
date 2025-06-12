class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars)==1: return 1
        
        def write(letter, amt, i):
            if amt==1:
                chars[i] = letter
                return i+1
            amt = list(str(amt))
            chars[i] = letter
            for j in range(len(amt)):
                chars[i+1+j] = amt[j]
            return i+1+len(amt) # return new start index

        curr_i=0
        curr_l = chars[0]
        amt = 1

        for i in range(1, len(chars)):
            letter = chars[i]

            if letter != curr_l:
                length = write(curr_l, amt, curr_i)
                print(f"wrote to {curr_i} with letter {curr_l}")
                print(f"ended at {length}")

                curr_i = length
                curr_l = letter
                amt = 1

                print("wrote to ")
            else: amt+=1
        
        print(chars)
        if amt > 0:
            print("got here")
            length = write(curr_l, amt, curr_i)
            return length

        
        return length
        

        


            
        