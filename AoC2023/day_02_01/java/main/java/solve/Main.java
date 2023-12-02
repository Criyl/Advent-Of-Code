package solve;

class Main {
    public static void main(String[] args) {

        Utils utils = new Utils();
        String content = utils.getResourceFileAsString("input.txt");

        System.out.println(Solver.solve(content));
    }
}