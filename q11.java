class Solution {
    public String convert(String s, int numRows) {
        if (numRows == 1 || numRows >= s.length()) return s;

      
        StringBuilder[] sb = new StringBuilder[numRows];
        for (int i = 0; i < numRows; i++) sb[i] = new StringBuilder();

        int r = 0, d = 1; 

        
        for (char c : s.toCharArray()) {
            sb[r].append(c);
            
            
            if (r == 0) d = 1;
            else if (r == numRows - 1) d = -1;
            
            r += d;
        }

        StringBuilder res = new StringBuilder();
        for (StringBuilder row : sb) res.append(row);

        return res.toString();
    }
}