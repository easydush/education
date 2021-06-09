import { Account } from "./user";

export interface Question {
  id: number;
  title: string;
  answers: Answer[];
}

export interface Answer {
  id: number;
  title: string;
  is_right: boolean;
}

export interface Lesson {
  id: number;
  title: string;
  text: string;
  questions: Question[];
}

export interface Module {
  id: number;
  title: string;
  lessons: Lesson[];
}

export interface Course {
  id: number;
  title: string;
  teacher: Account;
  listeners: string;
  is_joined: boolean;
  modules: Module[];
  points: number;
}
