import { Layout, Table } from 'antd';
import { HeaderCustom } from '../../components/Header';
import React, { useCallback, useEffect, useMemo, useState } from 'react';
import { InfoBlock, PageHeaderText, StyledContent, StyledPageHeader } from '../Main/styles';
import { Course } from "../../types/course";
import { authorize, getCourses, getMyCourses } from "../../api";
import { Link } from "react-router-dom";
import { ColumnsType } from "antd/lib/table";
import { getCurrentCourses, getMyCurrentCourses } from "../../utils";

export const MyCourses = () : JSX.Element => {
  const [loading, setLoading] = useState<boolean>(false);
  const [data, setData] = useState<Course[]>([]);
  const handleJoin = useCallback((values) => {
    authorize(values);
  }, []);
  const columns = useMemo(
    () =>
      [
        {
          title: 'Название',
          dataIndex: 'title',
          width: '20%',
          render: function renderName(value, record) {
            return (
              <p>
                {record.title}
              </p>
            );
          },
          sorter: (a, b) => a.title.localeCompare(b.title),
        },
        {
          title: 'Преподаватель',
          dataIndex: 'teacher',
          render: function renderTeacher(value, record) {
            return (
              <p>
                {record.teacher.name}
              </p>
            );
          },
          sorter: (a, b) => a?.teacher?.name?.localeCompare(b.teacher.name),
        },
        {
          title: '',
          dataIndex: 'join',
          render: function renderJoin(value, record) {
            return (
              <Link to='/' onClick={handleJoin}>
                Присоединиться
              </Link>);
          },
        },
      ] as ColumnsType<Course>,
    [],
  );
  useEffect(() => {
    async function getData() {
      setLoading(true);
      await setTimeout(() => {
        getMyCourses();
        setData(getMyCurrentCourses() ?? []);
        setLoading(false);
      }, 500);
    }

    getData();
  }, []);
  return (
    <Layout>
      <HeaderCustom />
      <StyledContent>
        <StyledPageHeader title={<PageHeaderText>Курсы</PageHeaderText>} backIcon={false} />
        <InfoBlock>
          <Table<Course>
            columns={columns}
            dataSource={data}
            loading={loading}
            pagination={{ pageSize: 7 }}
          />
        </InfoBlock>
      </StyledContent>
    </Layout>
  );
}
