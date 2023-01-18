package main

import (
	"fmt"
	"regexp"
	"strings"
)

// sanitize based on this: https://owasp.org/www-community/password-special-characters
func main() {
	// sanitizedName := "riset.ai_riset.ai@trial-NoMask"
	sanitizedName := `!@#$%^&*()\{}[]~/.<>?,_:;'` + "`"
	sanitizedName = strings.ReplaceAll(sanitizedName, `!`, "excl")
	sanitizedName = strings.ReplaceAll(sanitizedName, `#`, "hash")
	sanitizedName = strings.ReplaceAll(sanitizedName, `$`, "dollar")
	sanitizedName = strings.ReplaceAll(sanitizedName, `%`, "percent")
	sanitizedName = strings.ReplaceAll(sanitizedName, `&`, "amprsand")
	sanitizedName = strings.ReplaceAll(sanitizedName, `'`, "squote")
	sanitizedName = strings.ReplaceAll(sanitizedName, `(`, "lprths")
	sanitizedName = strings.ReplaceAll(sanitizedName, `)`, "rprths")
	sanitizedName = strings.ReplaceAll(sanitizedName, `*`, "astrk")
	sanitizedName = strings.ReplaceAll(sanitizedName, `+`, "plus")
	sanitizedName = strings.ReplaceAll(sanitizedName, `,`, "comma")
	sanitizedName = strings.ReplaceAll(sanitizedName, `-`, "minus")
	sanitizedName = strings.ReplaceAll(sanitizedName, `.`, "dot")
	sanitizedName = strings.ReplaceAll(sanitizedName, `/`, "slash")
	sanitizedName = strings.ReplaceAll(sanitizedName, `:`, "colon")
	sanitizedName = strings.ReplaceAll(sanitizedName, `;`, "scolon")
	sanitizedName = strings.ReplaceAll(sanitizedName, `<`, "lthan")
	sanitizedName = strings.ReplaceAll(sanitizedName, `=`, "equal")
	sanitizedName = strings.ReplaceAll(sanitizedName, `>`, "gthan")
	sanitizedName = strings.ReplaceAll(sanitizedName, `?`, "qstion")
	sanitizedName = strings.ReplaceAll(sanitizedName, `@`, "at")
	sanitizedName = strings.ReplaceAll(sanitizedName, `[`, "lbracket")
	sanitizedName = strings.ReplaceAll(sanitizedName, `\`, "bslash")
	sanitizedName = strings.ReplaceAll(sanitizedName, `]`, "rbracket")
	sanitizedName = strings.ReplaceAll(sanitizedName, `^`, "caret")
	// sanitizedName = strings.ReplaceAll(sanitizedName, `_`, "uscore") // underscore is a legal character, so not replaced
	sanitizedName = strings.ReplaceAll(sanitizedName, "`", "btick")
	sanitizedName = strings.ReplaceAll(sanitizedName, `{`, "lbrace")
	sanitizedName = strings.ReplaceAll(sanitizedName, `|`, "vbar")
	sanitizedName = strings.ReplaceAll(sanitizedName, `}`, "rbrace")
	sanitizedName = strings.ReplaceAll(sanitizedName, `~`, "tilde")
	sanitizedName = regexp.MustCompile(`[^a-zA-Z0-9_]+`).ReplaceAllString(sanitizedName, "_")
	sanitizedName = strings.ToLower(sanitizedName)
	fmt.Println(sanitizedName)
	
}