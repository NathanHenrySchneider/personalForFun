public class Degree {

    public int degreeValue = 0;

    public Degree(String[] args) {

    }
    public void increaseDegree() {
        this.degreeValue += 1;
    }

    public void decreaseDegree() {
        this.degreeValue -=1;
    }

    public String toString() {
        return String.valueOf(this.degreeValue);
    }

    public void setDegreeValue(int temp) {
        this.degreeValue = temp;
    }
}
