import { Account } from "./user";
import { UserInfo } from "os";

export interface Course {
  id: number;
  title: string;
  teacher: Account;
  listeners: string;
}
