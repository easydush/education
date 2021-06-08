import { Account } from "./user";

export interface Course {
  id: number;
  title: string;
  teacher: Account;
}
