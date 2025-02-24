function calculateExpense() {
    let landCost = parseFloat(document.getElementById("landCost").value) || 0;
    let seedCost = parseFloat(document.getElementById("seedCost").value) || 0;
    let sowingCost = parseFloat(document.getElementById("sowingCost").value) || 0;
    let wateringCost = parseFloat(document.getElementById("wateringCost").value) || 0;
    let fertilizerCost = parseFloat(document.getElementById("fertilizerCost").value) || 0;
    let labourCost = parseFloat(document.getElementById("labourCost").value) || 0;
    let harvestingCost = parseFloat(document.getElementById("harvestingCost").value) || 0;
    let transportCost = parseFloat(document.getElementById("transportCost").value) || 0;
    let storageCost = parseFloat(document.getElementById("storageCost").value) || 0;

    let totalExpenses = landCost + seedCost + sowingCost + wateringCost + fertilizerCost + labourCost + harvestingCost + transportCost + storageCost;
    

    document.getElementById("totalExpense").innerHTML = `Total Expenses: <span style="color:blue;">₹${totalExpenses}</span>`;
}

// export const  a = totalExpenses;