import sys
import ExerciseTwo.helloworld as exercisetwo


def main(argv):
    if len(argv) == 0:
        exercisetwo.helloworld()
    else:
        exercisetwo.helloworld(argv[0])


if __name__ == '__main__':
    main(sys.argv[1:])
