{
    // code --list-extensions

  // ===== General Config =====
  "files.autoSave": "afterDelay",
  "security.workspace.trust.untrustedFiles": "open",
  "workbench.colorTheme": "Dracula Theme",
  "workbench.editor.empty.hint": "hidden",

  // ===== Git, GitHub & Copilot =====
  "git.autofetch": true,
  "github.copilot.enable": {
    "*": false
  },

  // ===== Native Formatter =====
  "[typescript]": {
    "editor.defaultFormatter": "vscode.typescript-language-features"
  },
  "[json]": {
    "editor.defaultFormatter": "vscode.json-language-features"
  },


  // ===== Error Lens Config =====
  "workbench.colorCustomizations": {
    "editorError.foreground": "#ff79c6",
    "editorWarning.foreground": "#FFB86C",
    "editorInfo.foreground": "#8be8fd64",

    "errorLens.errorForeground": "#ff79c6",
    "errorLens.warningForeground": "#FFB86C",
    "errorLens.infoForeground": "#8be8fd64",
    "errorLens.hintForeground": "#BD93F9",

    "errorLens.errorBackground": "#ff79c51f",
    "errorLens.warningBackground": "#443522",
    "errorLens.infoBackground": "#8be8fd1c",
    "errorLens.hintBackground": "#292D3E",

    "errorLens.errorMessageBackground": "#ff79c51f",
    "errorLens.warningMessageBackground": "#443522",
    "errorLens.infoMessageBackground": "#223344",
    "errorLens.hintMessageBackground": "#292D3E"
  },

  // ===== Editor Config =====
  "editor.formatOnSave": false,
  "editor.renderWhitespace": "all",

  "[c]": {
    "editor.tabSize": 4,
    "editor.insertSpaces": false,
  },
  "[h]": {
    "editor.tabSize": 4,
    "editor.insertSpaces": false,
  },
  "[python]": {
    "editor.tabSize": 4,
    "editor.insertSpaces": true,
  },

  // ===== Files Config =====
  "files.trimTrailingWhitespace": true,
  "files.insertFinalNewline": true,
  "files.exclude": {
    "**/*.o": true
  },

  // ===== Python Config =====
  "python.createEnvironment.trigger": "off",

  // ===== Spell Checker Config =====
  "cSpell.language": "en,es",
  "cSpell.userWords": [
    "flake8",
    "mypy",
    "PostgreSQL",
    "pycache",
    "pyenv",
    "pyproject",
    "subfolders",
    "venv"
  ],
}



    // "python.defaultInterpreterPath": "/opt/pyenv/versions/3.13.1/bin/python3",
    // "python.analysis.typeCheckingMode": "off",
    // "python.createEnvironment.trigger": "off",

    // "flake8.path": [
    //     "/home/iualkhim/.local/bin/flake8"
    // ],
    // "flake8.importStrategy": "fromEnvironment",
    // "flake8.interpreter": ["/opt/pyenv/versions/3.13.1/bin/python3"],

    // "mypy-type-checker.path": [
    //     "/home/iualkhim/.local/bin/mypy"
    // ],
    // "mypy-type-checker.args": [
    //     "--strict"
    // ],
    // "mypy-type-checker.importStrategy": "fromEnvironment",
    // "mypy-type-checker.interpreter": ["/opt/pyenv/versions/3.13.1/bin/python3"],
    // "files.autoSave": "afterDelay"

