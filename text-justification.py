class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
            
        justified_text = []
        
        # get groups of words :) 
        
        current_group = ""
        
        for word in words:
            
            if current_group and len(current_group) + 1 + len(word) > maxWidth:

                justified_text.append(current_group)
                current_group = ""
            
            if current_group:
                current_group += " "
                
            current_group += word
        
        if current_group:
            
            justified_text.append(current_group)
        
        # justify each row
        
        for j, row in enumerate(justified_text[:-1]):
            
            tokens = row.split(" ")
            
            if len(tokens) == 1:

                spaces = " " * (maxWidth - len(tokens[0]))

                tokens.append(spaces)

                justified_text[j] = "".join(tokens)

            else:

                length = sum(list(map(lambda x: len(x), tokens)))

                spaces = " " * (maxWidth - length)

                if len(spaces) % (len(tokens) - 1) == 0:

                    spacer = " " * (len(spaces)//(len(tokens)-1))

                    justified_text[j] = spacer.join(tokens)


                else:

                    spacers = [""] * (len(tokens) - 1)

                    for i in range(len(spaces)):

                        spacers[i % len(spacers)] += " "

                    adjusted_tokens = list(map(lambda x: x[0] + x[1], zip(tokens[:-1], spacers)))

                    adjusted_tokens.append(tokens[-1])

                    justified_text[j] = "".join(adjusted_tokens)

                
        tokens = justified_text[-1]

        length = sum(list(map(lambda x: len(x), tokens)))

        tokens += (" " * (maxWidth - length))

        justified_text[-1] = "".join(tokens)

        return(justified_text)
