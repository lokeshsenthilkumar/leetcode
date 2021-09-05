class Solution {
    public int numberOfWeakCharacters(int[][] properties) {
        
        int n = properties.length;
        int ans = 0;
        
        Arrays.sort(properties, (a, b) -> (a[0] == b[0]) ? (a[1] - b[1]) : b[0] - a[0]);
        
        int curr_max = 0;
        for (int i = 0; i < n; i++) {
            
            if (properties[i][1] < curr_max)
                ans++;
            else
                curr_max = Math.max(curr_max, properties[i][1]);
        }
        return ans;
    }
}