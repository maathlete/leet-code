class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        if len(strs) < 2:
            
            return([strs])
        
        else:
            
            set_maps = {}
            annagrams = {}
            
            for string in strs:
                
                key = sorted(list(string))
                
                if key in set_maps.values():
                    
                    ID = list(set_maps.values()).index(key) + 1
                    annagrams[ID] = annagrams[ID] + [string]
                    
                
                else:
                    
                    try:
                        ID = max(set_maps.keys()) + 1
                    except:
                        ID = 1
                        
                    set_maps[ID] = key
                    annagrams[ID] = [string]
            
            return(list(annagrams.values()))
                
