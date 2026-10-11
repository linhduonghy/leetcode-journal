
func encoding(s string) string {

	var arr []string

	n := len(s)

	i := 0

	for i < n {

		j := i

		for ; j+1 < n && s[i] == s[j+1]; j++ {

		}

		arr = append(arr, strconv.Itoa(j-i+1), string(s[i]))

		i = j + 1

	}

	return strings.Join(arr, "")

}

func countAndSay(n int) string {

	cur := "1"

	for i := 0; i < n-1; i++ {

		cur = encoding(cur)

	}

	return cur

}


 