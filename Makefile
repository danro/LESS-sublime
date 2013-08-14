# Mac OSX helpers for PLUTIL(1)

# JSON -> tmLanguage
.PHONY: jsontm
jsontm:
	plutil -convert xml1 LESS.tmLanguage.json -o LESS.tmLanguage

# tmLanguage -> JSON
.PHONY: tmjson
tmjson:
	plutil -convert json -r LESS.tmLanguage -o LESS.tmLanguage.json
