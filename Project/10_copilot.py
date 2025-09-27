import java.io.*;
import java.util.*;

public class StudentTest {
    public static void main(String[] args) throws IOException {
        HashMap<String, String[]> students = new HashMap<>();
        ArrayList<Double> gpas = new ArrayList<>();

        BufferedReader reader = new BufferedReader(new FileReader("students.csv"));
        String line = reader.readLine(); // skip header

        while ((line = reader.readLine()) != null) {
            String[] parts = line.split(",");
            students.put(parts[0], new String[]{parts[1], parts[2], parts[3]});
            gpas.add(Double.parseDouble(parts[2]));
        }
        reader.close();

        double sum = 0;
        for (double gpa : gpas) {
            sum += gpa;
        }
        double averageGpa = sum / gpas.size();
        System.out.println("Average GPA: " + String.format("%.2f", averageGpa));

        System.out.println("Above average students:");
        for (Map.Entry<String, String[]> entry : students.entrySet()) {
            double gpa = Double.parseDouble(entry.getValue()[1]);
            if (gpa > averageGpa) {
                System.out.println(entry.getKey() + " " + entry.getValue()[0] + " " + entry.getValue()[1]);
            }
        }

        System.out.println("Students who earned a scholarship:");
        for (Map.Entry<String, String[]> entry : students.entrySet()) {
            if (entry.getValue()[2].equals("Yes")) {
                System.out.println(entry.getKey() + " " + entry.getValue()[0] + " " + entry.getValue()[1]);
            }
        }
    }
}