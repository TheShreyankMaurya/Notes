// 1. if-else Statement

if (age < 18) {
    console.log("You cannot vote.");
} else {
    console.log("You can vote.");
}

// 2. nested if-else Statement

if (age > 18) {
    if ((license = true)) {
        console.log("You can drive on public road");
    } else {
        console.log("You cannot drive on public road");
    }
} else {
    console.log("You cannot apply for license");
}

// 3. switch

switch (color) {
    case "red":
        console.log("Stop");
        break;

    case "yellow":
        console.log("Slow Down");
        break;

    case "green":
        console.log("Go");
        break;

    default:
        console.log("Check and Go");
}
