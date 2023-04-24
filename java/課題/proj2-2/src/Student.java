
public class Student {
	String name;
	int score;
	static final int MAX_SCORE = 100;
	
	
	Student(String name, int score) {
		this.name = name;
		this.score = score;
	}
	
	Student(String name){
		this(name, 0);
	}
	
	//string型のgrade関数の追加
	String Grade() {
		if (score >= 90) {
			return "A+";
		}else if(score >= 80) {
			return "A";
		}else if(score >= 70) {
			return "B";
		}else if(score >= 60) {
			return "C";
		}else {
			return "D";
		}
	}
	
	void printScore() {
		System.out.println(name + "さんは" + MAX_SCORE + "点満点中、" +  score + "点で、成績は" + Grade() + "です。");
	}
}

class StudentSample{
	public static void main(String... args) {
		//murataインスタンス作成
		Student murata = new Student("村田");
		murata.score = 80;
		murata.printScore();
		
		//okadaインスタンス作成
		Student okada = new Student("岡田");
		okada.score = 90;
		okada.printScore();
		
		//suzukiインスタンス作成
		Student suzuki = new Student("鈴木");
		suzuki.score = 70;
		suzuki.printScore();
		
		//satouインスタンス作成
		Student satou = new Student("佐藤");
		satou.score = 65;
		satou.printScore();
		
		//yamadaインスタンス作成
		Student yamada = new Student("山田");
		yamada.score = 55;
		yamada.printScore();
		
	}
}
