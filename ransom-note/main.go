func canConstruct(ransomNote string, magazine string) bool {
    rnMap := map[rune]int{}
    for _, r := range ransomNote {
        rnMap[r] += 1
    }
    mMap := map[rune]int{}
    for _, r := range magazine {
        mMap[r] += 1
    }

    for key, val := range rnMap {
        if mMap[key] != val {
            return false
        }
    }
    return true
}
