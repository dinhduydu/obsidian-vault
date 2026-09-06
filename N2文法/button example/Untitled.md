# 🏠 Study App

```dataviewjs
const button = dv.el("button", "📚 あげる");

button.style.padding = "10px 20px";
button.style.fontSize = "16px";
button.style.cursor = "pointer";

button.onclick = () => {
    app.workspace.openLinkText(
        "あげる",
        "",
        false
    );
};
```
