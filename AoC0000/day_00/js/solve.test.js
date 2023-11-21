const solver = require('./solve.js')

describe("Solve Tests", () =>{
    test("Check literal value", () => {
        expect( solver.solve("Test Case") ).toBe("Hello, World");
    })
});