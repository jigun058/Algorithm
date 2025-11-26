var variable = 20
let constant = 10.1
let char = "taegwon"
print("Hello, \(char)!")

var arr = [1, 2, 3]
var dic = ["a": 1, "b": 2, "c": 3]      //키 하나마다 값이 한 개만 되는건가?

if arr[0] <= 5 {
    print("5 이하")
} else {
    print("5 초과")
}

for num in 1...10 {     //이게 range함수?
    print(num)
}

var count = 5
while count < 8 {
    print(count)
    count += 1
}

func add(a : Int, b : Int = 5) -> Int {
    return a + b
}

print(add(a: 3, b: 4))
print(add(a: 1))

class Person {
    var name: String
    var age: Int

    init(){
        self.name = "익명"
        self.age = -1
    }

    init(name: String, age: Int) {      //이건 안쓰면 자동으로 안 되나?
        self.name = name
        self.age = age
    }

    func profile() {
        print("이름 : \(name), 나이 : \(age)")
        print(name, age)
    }
}

let person = Person()
person.profile()

let me = Person(name: "태권", age: 24)
me.profile()

struct GuZoChae {
    var x: Int
    var y: Int

    func display(){
        print("좌표 : (\(x), \(y))")
    }
}

// 클래스는 레퍼런스 타입, 구조체는 값 타입. 상속 O/X.
var point = GuZoChae(x: 10, y: 5)
point.display()

enum Direction {
    case north
    case south
    case west
    case east
}

var dir = Direction.north
print(dir)

// ?로 옵셔널 변수
var optionalValue:Int? = nil

if let value = optionalValue {
    print("값은 \(value) 입니다.")
} else {
    print("값이 없습니다.")
}

let square = { (num: Int) -> Int in
    return num * num
}
print(square(5))

// 짧은 클로저
let nums = [6, 2, 8, 5, 1]
let sortedNums = nums.sorted { $0 < $1 }    // 클로저의 첫 번쨰, 두 번째 인수 - 숏핸드 인자 이름
print(sortedNums)