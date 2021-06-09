import { Account } from "./user";

export interface Question {
  id: number;
  title: string;
}

export interface Answer {
  id: number;
  question: Question;
  title: string;
  is_right: boolean;
}

export interface Lesson {
  id: number;
  title: string;
  text: string;
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
}
