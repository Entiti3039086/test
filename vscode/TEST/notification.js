requestPermission(postMessage)
requestPermission(sendNotification);
if (Notification.permission !== "granted") {
    Notification.requestPermission().then((permission) => {
        if (permission !== "granted") {
            console.log("Notifications are disabled.");
        }
    });
}

function sendNotification(message) {
    if (Notification.permission === "granted") {
        new Notification("Tab Activity", {
            body: message,
        });
    }
}

document.addEventListener("visibilitychange", () => {
    if (document.hidden) {
        sendNotification("You switched away from the tab!");
    } else {
        sendNotification("Welcome back to the tab!");
    }
});